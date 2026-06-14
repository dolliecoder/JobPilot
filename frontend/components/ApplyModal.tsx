'use client'

import { useState, useEffect } from 'react'
import { Job, Resume } from '@/types'
import { resumeApi, applicationApi } from '@/services/api'

interface ApplyModalProps {
  job: Job
  onClose: () => void
}

export default function ApplyModal({ job, onClose }: ApplyModalProps) {
  const [resumes, setResumes] = useState<Resume[]>([])
  const [selectedResumeId, setSelectedResumeId] = useState<number | null>(null)
  const [loading, setLoading] = useState(true)
  const [applying, setApplying] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [success, setSuccess] = useState(false)

  // Fetch resumes when modal mounts
  useEffect(() => {
    fetchResumes()
  }, []) // Empty dependency - only run on mount

  const fetchResumes = async () => {
    try {
      setLoading(true)
      setError(null)
      const data = await resumeApi.list()
      setResumes(data)
      if (data.length > 0) {
        setSelectedResumeId(data[0].id)
      } else {
        setSelectedResumeId(null)
      }
    } catch (err) {
      setError('Failed to load resumes')
      setResumes([])
      setSelectedResumeId(null)
    } finally {
      setLoading(false)
    }
  }

  const handleApply = async () => {
    if (!selectedResumeId) {
      setError('Please select a resume')
      return
    }

    setApplying(true)
    setError(null)

    try {
      await applicationApi.create(selectedResumeId, job.id)
      setSuccess(true)
      setTimeout(() => {
        onClose()
      }, 2000)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to submit application')
    } finally {
      setApplying(false)
    }
  }

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.5)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 1000
    }}>
      <div style={{
        backgroundColor: 'white',
        padding: '2rem',
        borderRadius: '8px',
        maxWidth: '500px',
        width: '90%',
        maxHeight: '80vh',
        overflow: 'auto'
      }}>
        <h3 style={{ marginTop: 0 }}>Apply to {job.title}</h3>
        <p style={{ color: '#666', marginBottom: '1.5rem' }}>
          {job.company} - {job.location}
        </p>

        {success ? (
          <div style={{
            padding: '1rem',
            backgroundColor: '#d4edda',
            color: '#155724',
            borderRadius: '4px',
            marginBottom: '1rem'
          }}>
            ✓ Application submitted successfully!
          </div>
        ) : (
          <>
            {loading ? (
              <div style={{ textAlign: 'center', padding: '2rem' }}>
                <p>Loading resumes...</p>
              </div>
            ) : resumes.length === 0 ? (
              <div>
                <p style={{ color: '#856404', backgroundColor: '#fff3cd', padding: '1rem', borderRadius: '4px' }}>
                  You need to upload a resume first before applying.
                </p>
                <div style={{ marginTop: '1rem', display: 'flex', gap: '0.5rem' }}>
                  <button
                    onClick={() => {
                      // Save job ID in URL for return navigation
                      window.location.href = `/upload?returnTo=jobs&jobId=${job.id}`
                    }}
                    style={{
                      padding: '0.75rem 1.5rem',
                      backgroundColor: '#0070f3',
                      color: 'white',
                      border: 'none',
                      borderRadius: '4px',
                      cursor: 'pointer'
                    }}
                  >
                    Upload Resume
                  </button>
                  <button
                    onClick={onClose}
                    style={{
                      padding: '0.75rem 1.5rem',
                      backgroundColor: '#ccc',
                      color: '#333',
                      border: 'none',
                      borderRadius: '4px',
                      cursor: 'pointer'
                    }}
                  >
                    Cancel
                  </button>
                </div>
              </div>
            ) : (
              <>
                <div style={{ marginBottom: '1.5rem' }}>
                  <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 'bold' }}>
                    Select Resume:
                  </label>
                  <select
                    value={selectedResumeId || ''}
                    onChange={(e) => setSelectedResumeId(Number(e.target.value))}
                    style={{
                      width: '100%',
                      padding: '0.75rem',
                      border: '1px solid #ccc',
                      borderRadius: '4px',
                      fontSize: '1rem'
                    }}
                  >
                    {resumes.map((resume) => (
                      <option key={resume.id} value={resume.id}>
                        {resume.filename} (uploaded {new Date(resume.uploaded_at).toLocaleDateString()})
                      </option>
                    ))}
                  </select>
                  <p style={{ fontSize: '0.875rem', color: '#666', marginTop: '0.5rem' }}>
                    {resumes.length} resume{resumes.length !== 1 ? 's' : ''} available
                  </p>
                </div>

                {error && (
                  <div style={{
                    padding: '1rem',
                    backgroundColor: '#f8d7da',
                    color: '#721c24',
                    borderRadius: '4px',
                    marginBottom: '1rem'
                  }}>
                    {error}
                  </div>
                )}

                <div style={{ display: 'flex', gap: '0.5rem', justifyContent: 'flex-end' }}>
                  <button
                    onClick={onClose}
                    disabled={applying}
                    style={{
                      padding: '0.75rem 1.5rem',
                      backgroundColor: '#ccc',
                      color: '#333',
                      border: 'none',
                      borderRadius: '4px',
                      cursor: applying ? 'not-allowed' : 'pointer'
                    }}
                  >
                    Cancel
                  </button>
                  <button
                    onClick={handleApply}
                    disabled={applying || !selectedResumeId}
                    style={{
                      padding: '0.75rem 1.5rem',
                      backgroundColor: applying || !selectedResumeId ? '#ccc' : '#28a745',
                      color: 'white',
                      border: 'none',
                      borderRadius: '4px',
                      cursor: applying || !selectedResumeId ? 'not-allowed' : 'pointer'
                    }}
                  >
                    {applying ? 'Submitting...' : 'Submit Application'}
                  </button>
                </div>
              </>
            )}
          </>
        )}
      </div>
    </div>
  )
}
