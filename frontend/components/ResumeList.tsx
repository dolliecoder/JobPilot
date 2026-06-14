'use client'

import { useState, useEffect } from 'react'
import { resumeApi } from '@/services/api'
import { Resume } from '@/types'

export default function ResumeList() {
  const [resumes, setResumes] = useState<Resume[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [deleting, setDeleting] = useState<number | null>(null)

  const fetchResumes = async () => {
    try {
      setLoading(true)
      setError(null)
      const data = await resumeApi.list()
      setResumes(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load resumes')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchResumes()
  }, [])

  const handleDelete = async (id: number, filename: string) => {
    if (!confirm(`Are you sure you want to delete "${filename}"?`)) {
      return
    }

    setDeleting(id)
    try {
      await resumeApi.delete(id)
      setResumes(resumes.filter(r => r.id !== id))
    } catch (err) {
      alert(err instanceof Error ? err.message : 'Failed to delete resume')
    } finally {
      setDeleting(null)
    }
  }

  const formatDate = (dateString: string) => {
    const date = new Date(dateString)
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString()
  }

  if (loading) {
    return <div>Loading resumes...</div>
  }

  if (error) {
    return (
      <div style={{ color: '#721c24', backgroundColor: '#f8d7da', padding: '1rem', borderRadius: '4px' }}>
        Error: {error}
      </div>
    )
  }

  if (resumes.length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem', color: '#666' }}>
        No resumes uploaded yet. Upload your first resume above!
      </div>
    )
  }

  return (
    <div style={{ marginTop: '2rem' }}>
      <h3>Uploaded Resumes ({resumes.length})</h3>
      <table style={{ 
        width: '100%', 
        borderCollapse: 'collapse',
        marginTop: '1rem',
        border: '1px solid #ddd'
      }}>
        <thead>
          <tr style={{ backgroundColor: '#f5f5f5' }}>
            <th style={{ padding: '0.75rem', textAlign: 'left', borderBottom: '2px solid #ddd' }}>
              Filename
            </th>
            <th style={{ padding: '0.75rem', textAlign: 'left', borderBottom: '2px solid #ddd' }}>
              Upload Date
            </th>
            <th style={{ padding: '0.75rem', textAlign: 'center', borderBottom: '2px solid #ddd' }}>
              Actions
            </th>
          </tr>
        </thead>
        <tbody>
          {resumes.map((resume) => (
            <tr key={resume.id} style={{ borderBottom: '1px solid #ddd' }}>
              <td style={{ padding: '0.75rem' }}>
                {resume.filename}
              </td>
              <td style={{ padding: '0.75rem' }}>
                {formatDate(resume.uploaded_at)}
              </td>
              <td style={{ padding: '0.75rem', textAlign: 'center' }}>
                <button
                  onClick={() => handleDelete(resume.id, resume.filename)}
                  disabled={deleting === resume.id}
                  style={{
                    padding: '0.4rem 1rem',
                    backgroundColor: deleting === resume.id ? '#ccc' : '#dc3545',
                    color: 'white',
                    border: 'none',
                    borderRadius: '4px',
                    cursor: deleting === resume.id ? 'not-allowed' : 'pointer'
                  }}
                >
                  {deleting === resume.id ? 'Deleting...' : 'Delete'}
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
