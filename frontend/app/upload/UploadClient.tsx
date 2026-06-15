'use client'

import { useState, useEffect } from 'react'
import { useSearchParams, useRouter } from 'next/navigation'
import ResumeUpload from '@/components/ResumeUpload'
import ResumeList from '@/components/ResumeList'

export default function UploadClient() {
  const [refreshKey, setRefreshKey] = useState(0)
  const [showReturnMessage, setShowReturnMessage] = useState(false)
  const searchParams = useSearchParams()
  const router = useRouter()
  
  const returnTo = searchParams.get('returnTo')
  const jobId = searchParams.get('jobId')

  useEffect(() => {
    // Show message if coming from job application flow
    if (returnTo === 'jobs' && jobId) {
      setShowReturnMessage(true)
    }
  }, [returnTo, jobId])

  const handleUploadSuccess = () => {
    // Force ResumeList to refresh by changing key
    setRefreshKey(prev => prev + 1)
    
    // If user came from job application, redirect back with context
    if (returnTo === 'jobs' && jobId) {
      setTimeout(() => {
        // Add parameters to indicate resume was uploaded and which job to reopen
        router.push(`/jobs?resumeUploaded=true&jobId=${jobId}`)
      }, 1500) // Give time to see success message
    }
  }

  return (
    <div>
      <h2>Resume Management</h2>
      
      {showReturnMessage && (
        <div style={{
          padding: '1rem',
          backgroundColor: '#d1ecf1',
          color: '#0c5460',
          borderRadius: '4px',
          marginBottom: '1rem',
          border: '1px solid #bee5eb'
        }}>
          <strong>📄 Upload your resume to continue applying</strong>
          <p style={{ margin: '0.5rem 0 0 0', fontSize: '0.9rem' }}>
            After uploading, you'll be redirected back and the application form will reopen automatically.
          </p>
        </div>
      )}
      
      <ResumeUpload onUploadSuccess={handleUploadSuccess} />
      <ResumeList key={refreshKey} />
    </div>
  )
}
