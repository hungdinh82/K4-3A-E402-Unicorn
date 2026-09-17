import { CheckCheck, Clock3, ListTodo, Text } from 'lucide-react'
import type { NoteMoment } from '../services/notes'

function InfoSection({ title, lines, icon: Icon }: { title: string; lines: string[]; icon: typeof Text }) {
  if (!lines.length) return null
  return <div className="note-info"><div className="note-info-title"><Icon size={16}/><strong>{title}</strong></div><ul>{lines.map((line, index) => <li key={index}>{line}</li>)}</ul></div>
}
export function NoteMomentCard({ moment, defaultOpen }: { moment: NoteMoment; defaultOpen: boolean }) {
  return <details className="note-moment" open={defaultOpen ? true : undefined}><summary><span className="moment-index">{moment.id + 1}</span><span className="moment-heading"><strong>{moment.title}</strong><small>{moment.overview[0]}</small></span><span className="disclosure-chevron">⌄</span></summary><div className="moment-body"><InfoSection title="Tóm tắt" icon={Text} lines={moment.overview}/>{(moment.decisions.length > 0 || moment.actions.length > 0) && <div className="moment-grid"><InfoSection title="Quyết định" icon={CheckCheck} lines={moment.decisions}/><InfoSection title="Việc cần làm" icon={ListTodo} lines={moment.actions}/></div>}</div><span className="sr-only"><Clock3 size={1}/></span></details>
}
