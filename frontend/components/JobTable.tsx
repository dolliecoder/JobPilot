'use client'

import { Job } from '@/types'

interface JobTableProps {
  jobs: Job[]
  loading: boolean
}

export default function JobTable({ jobs, loading }: JobTableProps) {
  if (loading) {
    return <div style={{ textAlign: 'center', padding: '2rem' }}>Loading jobs...</div>
  }

  if (jobs.length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem', color: '#666' }}>
        No jobs found. Try adjusting your search criteria.
      </div>
    )
  }

  return (
    <div>
      <p style={{ marginBottom: '1rem', color: '#666' }}>
        Found {jobs.length} job{jobs.length !== 1 ? 's' : ''}
      </p>
      <table style={{ 
        width: '100%', 
        borderCollapse: 'collapse',
        border: '1px solid #ddd'
      }}>
        <thead>
          <tr style={{ backgroundColor: '#f5f5f5' }}>
            <th style={{ padding: '0.75rem', textAlign: 'left', borderBottom: '2px solid #ddd' }}>
              Title
            </th>
            <th style={{ padding: '0.75rem', textAlign: 'left', borderBottom: '2px solid #ddd' }}>
              Company
            </th>
            <th style={{ padding: '0.75rem', textAlign: 'left', borderBottom: '2px solid #ddd' }}>
              Location
            </th>
            <th style={{ padding: '0.75rem', textAlign: 'left', borderBottom: '2px solid #ddd' }}>
              Job Type
            </th>
          </tr>
        </thead>
        <tbody>
          {jobs.map((job) => (
            <tr key={job.id} style={{ borderBottom: '1px solid #ddd' }}>
              <td style={{ padding: '0.75rem' }}>
                <strong>{job.title}</strong>
              </td>
              <td style={{ padding: '0.75rem' }}>
                {job.company}
              </td>
              <td style={{ padding: '0.75rem' }}>
                {job.location}
              </td>
              <td style={{ padding: '0.75rem' }}>
                <span style={{
                  padding: '0.25rem 0.5rem',
                  backgroundColor: '#e3f2fd',
                  borderRadius: '4px',
                  fontSize: '0.875rem'
                }}>
                  {job.job_type}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
