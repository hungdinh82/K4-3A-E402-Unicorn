import { useEffect, useState } from 'react'
import { Circle, Monitor, Mic } from 'lucide-react'
import type { AppModel } from '../hooks/useAppModel'
import type { Appearance } from '../services/types'
import { desktop, type SummaryAiConfig } from '../services/desktop'

function SettingRow({ label, value }: { label: string; value: string }) { return <div className="setting-row"><span>{label}</span><strong>{value}</strong></div> }
export function SettingsPage({ model, appearance, setAppearance }: { model: AppModel; appearance: Appearance; setAppearance: (value: Appearance) => void }) {
  const [groqKey, setGroqKey] = useState('')
  const [groqStatus, setGroqStatus] = useState<'saved' | 'environment' | 'none' | 'loading'>('loading')
  const [groqMessage, setGroqMessage] = useState('')
  const [savingGroq, setSavingGroq] = useState(false)
  const [summaryConfig, setSummaryConfig] = useState<SummaryAiConfig>({ apiUrl: 'http://127.0.0.1:20128/v1', model: 'cx/gpt-5.5' })
  const [summaryMessage, setSummaryMessage] = useState('')
  const [savingSummary, setSavingSummary] = useState(false)
  useEffect(() => {
    if (!desktop.isDesktop) { setGroqStatus('none'); return }
    let active = true
    void desktop.groqKeyStatus().then(value => { if (active) setGroqStatus(value) })
      .catch(error => { if (active) setGroqMessage(`Không đọc được trạng thái key: ${error}`) })
    void desktop.getSummaryAiConfig().then(value => { if (active) setSummaryConfig(value) })
      .catch(error => { if (active) setSummaryMessage(`Không đọc được cấu hình: ${error}`) })
    return () => { active = false }
  }, [])
  const changeGroqKey = async (key: string | null) => {
    setSavingGroq(true); setGroqMessage('')
    try {
      const next = await desktop.setGroqApiKey(key)
      setGroqStatus(next); setGroqKey('')
      setGroqMessage(key ? 'Đã lưu key an toàn. ASR đang khởi động lại với Groq.' : 'Đã xóa key. ASR đang khởi động lại.')
    } catch (error) { setGroqMessage(`Không cập nhật được: ${error}`) }
    finally { setSavingGroq(false) }
  }
  const saveSummaryConfig = async () => {
    setSavingSummary(true); setSummaryMessage('')
    try {
      const next = await desktop.setSummaryAiConfig(summaryConfig)
      setSummaryConfig(next); setSummaryMessage('Đã lưu. Lần dịch và tóm tắt tiếp theo sẽ dùng cấu hình này.')
    } catch (error) { setSummaryMessage(`Không cập nhật được: ${error}`) }
    finally { setSavingSummary(false) }
  }
  const disabled = !desktop.isDesktop || savingGroq || model.capturing || model.meetingActive
  const summaryDisabled = !desktop.isDesktop || savingSummary || model.capturing || model.meetingActive
  return <main className="page-scroll"><div className="page-wrap settings-wrap animate-in"><div className="eyebrow">SYSTEM</div><h1>Cài đặt & trạng thái</h1><p className="page-subtitle">Các thành phần đang dùng trong prototype.</p>
    <section className="glass-card settings-card"><div className="settings-heading"><Circle size={19}/><h3>Giao diện</h3><small>Liquid Glass</small></div><div className="segmented appearance-picker">{([['system','Hệ thống'], ['light','Sáng'], ['dark','Tối']] as const).map(([key, label]) => <button key={key} className={appearance === key ? 'selected' : ''} onClick={() => setAppearance(key)}>{label}</button>)}</div><small className="muted">{appearance === 'system' ? 'Tự động theo giao diện hệ thống.' : appearance === 'light' ? 'Nền trắng hồng, ánh xanh băng và kính lavender.' : 'Nền tím đêm, ánh lavender và hồng phấn.'}</small></section>
    <section className="glass-card settings-card"><h3>Groq ASR · Whisper Large V3</h3><SettingRow label="API key" value={groqStatus === 'saved' ? 'Đã lưu trong kho mật khẩu hệ thống' : groqStatus === 'environment' ? 'Đang dùng biến môi trường GROQ_API_KEY' : groqStatus === 'loading' ? 'Đang kiểm tra…' : 'Chưa cấu hình · dùng ASR local'}/><label className="groq-key-label" htmlFor="groq-api-key">Nhập Groq API key</label><div className="groq-key-actions"><input id="groq-api-key" type="password" autoComplete="off" spellCheck={false} placeholder="gsk_…" value={groqKey} onChange={event => setGroqKey(event.target.value)} disabled={disabled}/><button className="pill-btn primary" disabled={disabled || !groqKey.trim()} onClick={() => void changeGroqKey(groqKey)}>Lưu key</button>{groqStatus === 'saved' && <button className="pill-btn" disabled={disabled} onClick={() => void changeGroqKey(null)}>Xóa key</button>}</div><small className="muted">Key không hiển thị lại. Đổi key khi đã dừng ghi âm; âm thanh sẽ được gửi tới Groq để nhận diện.</small>{groqMessage && <small role="status" className="groq-key-message">{groqMessage}</small>}</section>
    <section className="glass-card settings-card"><h3>Tóm tắt AI</h3><label className="groq-key-label" htmlFor="summary-api-url">API base URL</label><input id="summary-api-url" className="summary-config-input" type="url" spellCheck={false} placeholder="http://127.0.0.1:20128/v1" value={summaryConfig.apiUrl} onChange={event => setSummaryConfig(config => ({ ...config, apiUrl: event.target.value }))} disabled={summaryDisabled}/><label className="groq-key-label" htmlFor="summary-model">Model</label><div className="groq-key-actions"><input id="summary-model" type="text" spellCheck={false} placeholder="gpt-oss-120b" value={summaryConfig.model} onChange={event => setSummaryConfig(config => ({ ...config, model: event.target.value }))} disabled={summaryDisabled}/><button className="pill-btn primary" disabled={summaryDisabled || !summaryConfig.apiUrl.trim() || !summaryConfig.model.trim()} onClick={() => void saveSummaryConfig()}>Lưu cấu hình</button></div><small className="muted">Nhập API base URL theo chuẩn OpenAI, ví dụ: http://127.0.0.1:20128/v1. Không thay đổi khi đang ghi âm.</small>{summaryMessage && <small role="status" className="groq-key-message">{summaryMessage}</small>}</section>
    <section className="glass-card settings-card"><h3>Âm thanh & nhận diện</h3><SettingRow label="ASR" value={model.vietnameseASRStatus}/><SettingRow label="Fallback khi thiếu API key" value="Local PhoWhisper / Whisper Turbo"/><SettingRow label="Dịch theo đoạn" value={model.translationStatus}/><SettingRow label="TTS" value={model.ttsStatus}/><SettingRow label="Trạng thái" value={model.status}/><div className="permission-row"><button className="pill-btn" onClick={() => void desktop.openPermission('screen')}><Monitor size={15}/>Mở quyền ghi âm màn hình</button><button className="pill-btn" onClick={() => void desktop.openPermission('microphone')}><Mic size={15}/>Mở quyền microphone</button></div></section>
  </div></main>
}
