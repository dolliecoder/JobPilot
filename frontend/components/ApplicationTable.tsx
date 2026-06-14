'use client'

export default function ApplicationTable() {
  return (
    <table style={{ width: '100%', borderCollapse: 'collapse' }}>
      <thead>
        <tr style={{ borderBottom: '2px solid #ccc' }}>
          <th style={{ padding: '0.5rem', textAlign: 'left' }}>Job Title</th>
          <th style={{ padding: '0.5rem', textAlign: 'left' }}>Company</th>
          <th style={{ padding: '0.5rem', textAlign: 'left' }}>Match Score</th>
          <th style={{ padding: '0.5rem', textAlign: 'left' }}>Status</th>
          <th style={{ padding: '0.5rem', textAlign: 'left' }}>Applied Date</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colSpan={5} style={{ padding: '1rem', textAlign: 'center' }}>
            No applications yet
          </td>
        </tr>
      </tbody>
    </table>
  )
}
