'use client'

export default function JobTable() {
  return (
    <table style={{ width: '100%', borderCollapse: 'collapse' }}>
      <thead>
        <tr style={{ borderBottom: '2px solid #ccc' }}>
          <th style={{ padding: '0.5rem', textAlign: 'left' }}>Title</th>
          <th style={{ padding: '0.5rem', textAlign: 'left' }}>Company</th>
          <th style={{ padding: '0.5rem', textAlign: 'left' }}>Location</th>
          <th style={{ padding: '0.5rem', textAlign: 'left' }}>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colSpan={4} style={{ padding: '1rem', textAlign: 'center' }}>
            No jobs found
          </td>
        </tr>
      </tbody>
    </table>
  )
}
