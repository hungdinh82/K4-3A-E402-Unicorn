import { useEffect, useState } from 'react'
import { Circle, Monitor, Mic } from 'lucide-react'
import type { AppModel } from '../hooks/useAppModel'
import type { Appearance } from '../services/types'
import { desktop, type SummaryAiConfig, type SummaryAiProvider } from '../services/desktop'

type KeyStatus = 'saved' | 'environment' | 'none' | 'loading'

function SettingRow({ label, value }: { label: string; value: string }) {
  return <div className="setting-row"><span>{label}</span><strong>{value}</strong></div>
}

const NINE_ROUTER_MODEL: SummaryAiConfig = {
  provider: 'nine_router',
  apiUrl: 'http://127.0.0.1:20128/v1',
  model: 'cx/gpt-5.5',
}
const GROQ_GPT_OSS_120B: SummaryAiConfig = {
  provider: 'groq',
  apiUrl: 'https://api.groq.com/openai/v1',
  model: 'openai/gpt-oss-120b',
}

const keyStatusText = (provider: SummaryAiProvider, status: KeyStatus) => {
  if (status === 'saved') return 'Đã lưu trong kho mật khẩu hệ thống'
  if (status === 'environment') return `Đang dùng biến môi trường ${provider === 'groq' ? 'GROQ_API_KEY' : 'NINE_ROUTER_API_KEY'}`
  if (status === 'loading') return 'Đang kiểm tra…'
  return provider === 'groq' ? 'Chưa cấu hình' : 'Chưa lưu · vẫn dùng được nếu 9Router không yêu cầu key'
}

export function SettingsPage({ model, appearance, setAppearance }: { model: AppModel; appearance: Appearance; setAppearance: (value: Appearance) => void }) {
  const [apiKey, setApiKey] = useState('')
  const [keyStatuses, setKeyStatuses] = useState<Record<SummaryAiProvider, KeyStatus>>({ groq: 'loading', nine_router: 'loading' })
  const [keyMessage, setKeyMessage] = useState('')
  const [savingKey, setSavingKey] = useState(false)
  const [summaryConfig, setSummaryConfig] = useState<SummaryAiConfig>(NINE_ROUTER_MODEL)
  const [nineRouterDraft, setNineRouterDraft] = useState<SummaryAiConfig>(NINE_ROUTER_MODEL)
  const [summaryMessage, setSummaryMessage] = useState('')
  const [savingSummary, setSavingSummary] = useState(false)

  useEffect(() => {
    if (!desktop.isDesktop) {
      setKeyStatuses({ groq: 'none', nine_router: 'none' })
      return
    }
    let active = true
    void Promise.all([
      desktop.aiKeyStatus('groq'),
      desktop.aiKeyStatus('nine_router'),
      desktop.getSummaryAiConfig(),
    ]).then(([groq, nineRouter, config]) => {
      if (!active) return
      setKeyStatuses({ groq, nine_router: nineRouter })
      setSummaryConfig(config)
      if (config.provider === 'nine_router') setNineRouterDraft(config)
    }).catch(error => {
      if (active) setSummaryMessage(`Không đọc được cấu hình: ${error}`)
    })
    return () => { active = false }
  }, [])

  const provider = summaryConfig.provider
  const currentKeyStatus = keyStatuses[provider]
  const disabled = !desktop.isDesktop || savingKey || model.capturing || model.meetingActive
  const summaryDisabled = !desktop.isDesktop || savingSummary || model.capturing || model.meetingActive

  const changeApiKey = async (key: string | null) => {
    setSavingKey(true)
    setKeyMessage('')
    try {
      const next = await desktop.setAiApiKey(provider, key)
      const savedConfig = await desktop.setSummaryAiConfig(summaryConfig)
      setKeyStatuses(statuses => ({ ...statuses, [provider]: next }))
      setSummaryConfig(savedConfig)
      setApiKey('')
      setKeyMessage(key ? `Đã lưu key và chuyển sang ${provider === 'groq' ? 'Groq' : '9Router'}.` : 'Đã xóa API key.')
    } catch (error) {
      setKeyMessage(`Không cập nhật được: ${error}`)
    } finally {
      setSavingKey(false)
    }
  }

  const selectProvider = (next: SummaryAiProvider) => {
    setSummaryMessage('')
    setKeyMessage('')
    setApiKey('')
    setSummaryConfig(next === 'groq' ? GROQ_GPT_OSS_120B : nineRouterDraft)
  }

  const updateNineRouter = (field: 'apiUrl' | 'model', value: string) => {
    setSummaryConfig(config => ({ ...config, [field]: value }))
    setNineRouterDraft(config => ({ ...config, [field]: value }))
  }

  const saveSummaryConfig = async () => {
    setSavingSummary(true)
    setSummaryMessage('')
    try {
      const next = await desktop.setSummaryAiConfig(summaryConfig)
      setSummaryConfig(next)
      if (next.provider === 'nine_router') setNineRouterDraft(next)
      setSummaryMessage('Đã lưu. Lần dịch và tóm tắt tiếp theo sẽ dùng cấu hình này.')
    } catch (error) {
      setSummaryMessage(`Không cập nhật được: ${error}`)
    } finally {
      setSavingSummary(false)
    }
  }

  return <main className="page-scroll"><div className="page-wrap settings-wrap animate-in">
    <div className="eyebrow">SYSTEM</div>
    <h1>Cài đặt & trạng thái</h1>
    <p className="page-subtitle">Cấu hình dịch vụ AI và các thành phần của VietNote.</p>

    <section className="glass-card settings-card">
      <div className="settings-heading"><Circle size={19}/><h3>Giao diện</h3><small>Liquid Glass</small></div>
      <div className="segmented appearance-picker">{([['system','Hệ thống'], ['light','Sáng'], ['dark','Tối']] as const).map(([key, label]) => <button key={key} className={appearance === key ? 'selected' : ''} onClick={() => setAppearance(key)}>{label}</button>)}</div>
      <small className="muted">{appearance === 'system' ? 'Tự động theo giao diện hệ thống.' : appearance === 'light' ? 'Nền trắng hồng, ánh xanh băng và kính lavender.' : 'Nền tím đêm, ánh lavender và hồng phấn.'}</small>
    </section>

    <section className="glass-card settings-card">
      <h3>Tóm tắt & dịch AI</h3>
      <label className="groq-key-label" htmlFor="ai-provider">Nhà cung cấp API</label>
      <div className="groq-key-actions">
        <select id="ai-provider" value={provider} onChange={event => selectProvider(event.target.value as SummaryAiProvider)} disabled={summaryDisabled || savingKey}>
          <option value="nine_router">9Router · OpenAI-compatible</option>
          <option value="groq">Groq · GPT-OSS 120B</option>
        </select>
        <button className="pill-btn primary" disabled={summaryDisabled || !summaryConfig.apiUrl.trim() || !summaryConfig.model.trim()} onClick={() => void saveSummaryConfig()}>Lưu cấu hình</button>
      </div>

      <SettingRow label="API key" value={keyStatusText(provider, currentKeyStatus)}/>
      <label className="groq-key-label" htmlFor="ai-api-key">Nhập {provider === 'groq' ? 'Groq' : '9Router'} API key</label>
      <div className="groq-key-actions">
        <input id="ai-api-key" type="password" autoComplete="off" spellCheck={false} placeholder={provider === 'groq' ? 'gsk_…' : 'API key từ 9Router Dashboard'} value={apiKey} onChange={event => setApiKey(event.target.value)} disabled={disabled}/>
        <button className="pill-btn primary" disabled={disabled || !apiKey.trim()} onClick={() => void changeApiKey(apiKey)}>Lưu key</button>
        {currentKeyStatus === 'saved' && <button className="pill-btn" disabled={disabled} onClick={() => void changeApiKey(null)}>Xóa key</button>}
      </div>

      {provider === 'groq' ? <>
        <SettingRow label="Model ID" value={GROQ_GPT_OSS_120B.model}/>
        <SettingRow label="Endpoint" value={GROQ_GPT_OSS_120B.apiUrl}/>
        <small className="muted">Groq dùng reasoning mức thấp để tránh GPT-OSS tiêu hết token trước khi trả nội dung. Key này cũng được dùng cho Whisper ASR.</small>
      </> : <>
        <label className="groq-key-label" htmlFor="summary-api-url">API base URL</label>
        <input id="summary-api-url" className="summary-config-input" type="url" spellCheck={false} value={summaryConfig.apiUrl} onChange={event => updateNineRouter('apiUrl', event.target.value)} disabled={summaryDisabled}/>
        <label className="groq-key-label" htmlFor="summary-model">Model ID</label>
        <input id="summary-model" className="summary-config-input" type="text" spellCheck={false} value={summaryConfig.model} onChange={event => updateNineRouter('model', event.target.value)} disabled={summaryDisabled}/>
        <small className="muted">Mặc định dùng 9Router local tại 127.0.0.1:20128. API key là tùy chọn nếu server local không bật xác thực.</small>
      </>}
      {provider === 'groq' && currentKeyStatus === 'none' && <small className="groq-key-message">Cần lưu Groq API key trước khi chạy GPT-OSS 120B.</small>}
      {keyMessage && <small role="status" className="groq-key-message">{keyMessage}</small>}
      {summaryMessage && <small role="status" className="groq-key-message">{summaryMessage}</small>}
    </section>

    <section className="glass-card settings-card">
      <h3>Âm thanh & nhận diện</h3>
      <SettingRow label="ASR" value={model.vietnameseASRStatus}/>
      <SettingRow label="Groq ASR API" value={keyStatusText('groq', keyStatuses.groq)}/>
      <SettingRow label="Fallback khi thiếu API key" value="Local PhoWhisper / Whisper Turbo"/>
      <SettingRow label="Dịch theo đoạn" value={model.translationStatus}/>
      <SettingRow label="TTS" value={model.ttsStatus}/>
      <SettingRow label="Trạng thái" value={model.status}/>
      <div className="permission-row"><button className="pill-btn" onClick={() => void desktop.openPermission('screen')}><Monitor size={15}/>Mở quyền ghi âm màn hình</button><button className="pill-btn" onClick={() => void desktop.openPermission('microphone')}><Mic size={15}/>Mở quyền microphone</button></div>
    </section>
  </div></main>
}
