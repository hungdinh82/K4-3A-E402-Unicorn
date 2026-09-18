#!/usr/bin/env python3
"""Convert VinAI's PhoWhisper-medium checkpoint for local MLX inference."""

import json
import hashlib
import os
from pathlib import Path

import mlx.core as mx
import torch
# The Xet client can stall before creating its first range on some networks.
# Plain HTTP still provides atomic temporary files and metadata validation.
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')
from huggingface_hub import hf_hub_download
from mlx.utils import tree_flatten
from mlx_whisper.whisper import ModelDimensions, Whisper

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'vinai/PhoWhisper-medium'
REVISION = '55a7e3eb6c906de891f8f06a107754427dd3be79'
WEIGHTS_SHA256 = '699b8650035692ceb72db1d24c2879654e1cf9fa2d422a3bb14ac990b5141c59'
SOURCE_DIR = ROOT / '.cache' / 'models' / 'phowhisper-source'
DEST = ROOT / '.cache' / 'models' / 'phowhisper-medium-mlx'
EXPECTED_WEIGHTS_SIZE = 3055754969


def mlx_config(config):
    return dict(n_mels=config['num_mel_bins'],
                n_audio_ctx=config['max_source_positions'],
                n_audio_state=config['d_model'],
                n_audio_head=config['encoder_attention_heads'],
                n_audio_layer=config['encoder_layers'],
                n_vocab=config['vocab_size'],
                n_text_ctx=config['max_target_positions'],
                n_text_state=config['d_model'],
                n_text_head=config['decoder_attention_heads'],
                n_text_layer=config['decoder_layers'])


def mlx_key(key):
    key = key.removeprefix('model.')
    for old, new in (
        ('.layers', '.blocks'), ('.self_attn', '.attn'),
        ('.attn_layer_norm', '.attn_ln'),
        ('.encoder_attn_layer_norm', '.cross_attn_ln'),
        ('.encoder_attn.', '.cross_attn.'),
        ('.final_layer_norm', '.mlp_ln'),
        ('.q_proj', '.query'), ('.k_proj', '.key'),
        ('.v_proj', '.value'), ('.out_proj', '.out'),
        ('.fc1', '.mlp1'), ('.fc2', '.mlp2'),
        ('embed_positions.weight', 'positional_embedding'),
        ('decoder.embed_tokens', 'decoder.token_embedding'),
        ('encoder.layer_norm', 'encoder.ln_post'),
        ('decoder.layer_norm', 'decoder.ln'),
    ):
        key = key.replace(old, new)
    return key


def download(name):
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    target = SOURCE_DIR / name
    if name == 'pytorch_model.bin' and target.is_file() \
            and target.stat().st_size != EXPECTED_WEIGHTS_SIZE:
        # A redirected HTTP range request can be answered with the whole object;
        # curl -C then appends it to the partial file. Preserve the bad file for
        # diagnosis instead of silently deleting several GB of user data.
        invalid = target.with_name(f'{target.name}.invalid-{target.stat().st_size}')
        if invalid.exists():
            invalid = target.with_name(f'{target.name}.invalid-{target.stat().st_size}-{target.stat().st_mtime_ns}')
        target.replace(invalid)
        print(f'Preserved invalid checkpoint as {invalid.name}', flush=True)
    if not target.is_file():
        print(f'Downloading pinned {SOURCE}/{name} with verified Hub metadata…', flush=True)
        downloaded = Path(hf_hub_download(repo_id=SOURCE, filename=name,
                                          revision=REVISION, local_dir=SOURCE_DIR))
        if downloaded != target:
            downloaded.replace(target)
    if name == 'pytorch_model.bin' and target.stat().st_size != EXPECTED_WEIGHTS_SIZE:
        raise ValueError(f'PhoWhisper checkpoint size mismatch: {target.stat().st_size} '
                         f'!= {EXPECTED_WEIGHTS_SIZE}')
    return target


def install():
    if (DEST / 'config.json').is_file() and (DEST / 'weights.safetensors').is_file():
        print(f'PhoWhisper already installed: {DEST}', flush=True)
        return
    config_path = download('config.json')
    checkpoint = download('pytorch_model.bin')
    with checkpoint.open('rb') as file:
        digest = hashlib.file_digest(file, 'sha256').hexdigest()
    if digest != WEIGHTS_SHA256:
        raise ValueError(f'PhoWhisper checkpoint SHA-256 mismatch: {digest}')
    with config_path.open() as file:
        config = mlx_config(json.load(file))
    print('Converting PhoWhisper-medium to MLX float16…', flush=True)
    original = torch.load(checkpoint, map_location='cpu', weights_only=True)
    original.pop('proj_out.weight', None)  # Tied to decoder.token_embedding.
    original.pop('model.encoder.embed_positions.weight', None)  # MLX generates this sinusoid.
    weights = {}
    for name, value in original.items():
        key = mlx_key(name)
        if 'conv' in key and value.ndim == 3:
            value = value.transpose(1, 2)
        weights[key] = mx.array(value.numpy()).astype(mx.float16)
    del original
    model = Whisper(ModelDimensions(**config), mx.float16)
    expected = set(dict(tree_flatten(model.parameters())))
    # `alignment_heads` is a non-persistent runtime buffer in OpenAI Whisper.
    # Recent mlx-whisper versions expose it through parameters(), but it is not
    # part of Hugging Face checkpoints and is initialized by Whisper itself.
    expected.discard('alignment_heads')
    if set(weights) != expected:
        raise ValueError(f'Unexpected PhoWhisper weights: missing={sorted(expected - set(weights))[:10]}, '
                         f'extra={sorted(set(weights) - expected)[:10]}')
    del model
    DEST.mkdir(parents=True, exist_ok=True)
    temporary = DEST / 'weights.partial.safetensors'
    mx.save_safetensors(str(temporary), weights)
    with (DEST / 'config.json').open('w') as file:
        json.dump(config, file)
    temporary.replace(DEST / 'weights.safetensors')
    print(f'PhoWhisper ready: {DEST}', flush=True)


if __name__ == '__main__':
    install()
