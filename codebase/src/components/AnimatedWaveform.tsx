export function AnimatedWaveform({ compact = false, active = true }: { compact?: boolean; active?: boolean }) {
  return <span className={`animated-waveform ${compact ? 'compact' : ''} ${active ? 'active' : ''}`} aria-hidden="true">
    {[0, 1, 2, 3, 4].map(index => <span key={index} style={{ '--bar-index': index } as React.CSSProperties}/>) }
  </span>
}
