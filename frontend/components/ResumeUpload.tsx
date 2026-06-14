'use client'

import { useState } from 'react'
import { resumeApi } from '@/services/api'

interface ResumeUploadProps {
  onUploadSuccess?: () => void
}

export default function ResumeUpload({ onUploadSuccess }: ResumeUploadProps) {
  const [file, setFile] = useState<File | null>(null)
  const [uploading, setUploading] = useState(false)
  const [message, setMessage] = useState<{ type: 'success' | 'error', text: string } | null>(null)

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0]
    setMessage(null)
    
    if (!selectedFile) {
      setFile(null)
      return
    }
    
    // Validate file type
    if (!selectedFile.name.toLowerCase().endsWith('.pdf')) {
      setMessage({ type: 'error', text: 'Only PDF files are allowed' })
      setFile(null)
      return
    }
    
    // Validate file size (5MB)
    const maxSize = 5 * 1024 * 1024
    if (selectedFile.size > maxSize) {
      setMessage({ type: 'error', text: 'File size exceeds 5MB limit' })
      setFile(null)
      return
    }
    
    setFile(selectedFile)
  }

  const handleUpload = async () => {
    if (!file) {
      setMessage({ type: 'error', text: 'Please select a file first' })
      return
    }
    
    setUploading(true)
    setMessage(null)
    
    try {
      await resumeApi.upload(file)
      
      // Check if user is in the job application flow
      const urlParams = new URLSearchParams(window.location.search)
      const returnTo = urlParams.get('returnTo')
      
      if (returnTo === 'jobs') {
        setMessage({ type: 'success', text: `Resume "${file.name}" uploaded successfully! Redirecting back to jobs...` })
      } else {
        setMessage({ type: 'success', text: `Resume "${file.name}" uploaded successfully!` })
      }
      
      setFile(null)
      
      // Reset file input
      const fileInput = document.getElementById('resume-file-input') as HTMLInputElement
      if (fileInput) fileInput.value = ''
      
      // Callback to refresh list (and handle redirect if needed)
      if (onUploadSuccess) {
        onUploadSuccess()
      }
    } catch (error) {
      setMessage({ 
        type: 'error', 
        text: error instanceof Error ? error.message : 'Failed to upload resume' 
      })
    } finally {
      setUploading(false)
    }
  }

  return (
    <div>
      <div style={{ 
        border: '2px dashed #ccc', 
        padding: '2rem', 
        textAlign: 'center',
        borderRadius: '8px',
        backgroundColor: '#f9f9f9'
      }}>
        <p style={{ marginBottom: '1rem', color: '#666' }}>
          Upload your resume (PDF only, max 5MB)
        </p>
        <input 
          id="resume-file-input"
          type="file" 
          accept=".pdf" 
          onChange={handleFileChange}
          disabled={uploading}
          style={{ marginBottom: '1rem' }}
        />
        <br />
        <button 
          onClick={handleUpload}
          disabled={!file || uploading}
          style={{ 
            padding: '0.5rem 1.5rem',
            backgroundColor: !file || uploading ? '#ccc' : '#0070f3',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: !file || uploading ? 'not-allowed' : 'pointer',
            fontSize: '1rem'
          }}
        >
          {uploading ? 'Uploading...' : 'Upload Resume'}
        </button>
      </div>
      
      {message && (
        <div style={{ 
          marginTop: '1rem',
          padding: '1rem',
          borderRadius: '4px',
          backgroundColor: message.type === 'success' ? '#d4edda' : '#f8d7da',
          color: message.type === 'success' ? '#155724' : '#721c24',
          border: `1px solid ${message.type === 'success' ? '#c3e6cb' : '#f5c6cb'}`
        }}>
          {message.text}
        </div>
      )}
      
      {file && !message && (
        <div style={{ marginTop: '1rem', color: '#666' }}>
          Selected: {file.name} ({(file.size / 1024 / 1024).toFixed(2)} MB)
        </div>
      )}
    </div>
  )
}
