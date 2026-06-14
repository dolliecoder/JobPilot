'use client'

import { Application } from '@/types'

interface ApplicationTableProps {
  applications: Application[]
  loading: boolean
  onDelete: (id: number) => void
}

export default function ApplicationTable({ applications, loading, onDelete }: ApplicationTableProps) {
  const formatDate = (dateString: string) => {
    const date = new Date(dateString)
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString()
  }

  const getStatusColor = (status: string) => {
    const colors: { [key: string]: string } = {
      'Applied': '#e3f2fd',
      'Interviewing': '#fff3cd',
      'Accepted': '#d4edda',
      'Rejected': '#f8d7da'
    }
    return colors[status] || '#f5f5f5'
  }

  if (loading) {
    return <div style={{ textAlign: 'center', padding: '2rem' }}>Loading applications...</div>
  }

  if (applications.length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem', color: '#666' }}>
        <p>No applications yet.</p>
        <p>Browse jobs and apply to get started!</p>
        <button
          onClick={() => window.location.href = '/jobs'}
          style={{
            marginTop: '1rem',
            padding: '0.75rem 1.5rem',
            backgroundColor: '#0070f3',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
            fontSize: '1rem'
          }}
        >
          Browse Jobs
        </button>
      </div>
    )
  }

  return (
    <div>
      <p style={{ marginBottom: '1rem', color: '#666' }}>
        You have {applications.length} application{applications.length !== 1 ? 's' : ''}
      </p>
      <table style={{ 
        width: '100%', 
        borderCollapse: 'collapse',
        border: '1px solid #ddd'
      }}>
        <thead>
          <tr style={{ backgroundColor: '#f5f5f5' }}>
            <th style={{ padding: '0.75rem', textAlign: 'left', borderBottom: '2px solid #ddd' }}>
              Job Title
            </th>
            <th style={{ padding: '0.75rem', textAlign: 'left', borderBottom: '2px solid #ddd' }}>
              Company
            </th>
            <th style={{ padding: '0.75rem', textAlign: 'left', borderBottom: '2px solid #ddd' }}>
              Resume
            </th>
            <th style={{ padding: '0.75rem', textAlign: 'left', borderBottom: '2px solid #ddd' }}>
              Status
            </th>
            <th style={{ padding: '0.75rem', textAlign: 'left', borderBottom: '2px solid #ddd' }}>
              Applied Date
            </th>
            <th style={{ padding: '0.75rem', textAlign: 'center', borderBottom: '2px solid #ddd' }}>
              Actions
            </th>
          </tr>
        </thead>
        <tbody>
          {applications.map((app) => (
            <tr key={app.id} style={{ borderBottom: '1px solid #ddd' }}>
              <td style={{ padding: '0.75rem' }}>
                <strong>{app.job_title || 'Unknown'}</strong>
              </td>
              <td style={{ padding: '0.75rem' }}>
                {app.job_company || 'Unknown'}
              </td>
              <td style={{ padding: '0.75rem' }}>
                {app.resume_filename || 'Unknown'}
              </td>
              <td style={{ padding: '0.75rem' }}>
                <span style={{
                  padding: '0.25rem 0.75rem',
                  backgroundColor: getStatusColor(app.status),
                  borderRadius: '4px',
                  fontSize: '0.875rem'
                }}>
                  {app.status}
                </span>
              </td>
              <td style={{ padding: '0.75rem', fontSize: '0.875rem', color: '#666' }}>
                {formatDate(app.applied_at)}
              </td>
              <td style={{ padding: '0.75rem', textAlign: 'center' }}>
                <button
                  onClick={() => {
                    if (confirm('Are you sure you want to delete this application?')) {
                      onDelete(app.id)
                    }
                  }}
                  style={{
                    padding: '0.4rem 0.8rem',
                    backgroundColor: '#dc3545',
                    color: 'white',
                    border: 'none',
                    borderRadius: '4px',
                    cursor: 'pointer',
                    fontSize: '0.875rem'
                  }}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
