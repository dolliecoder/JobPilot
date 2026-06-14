'use client'

import { useState, useEffect } from 'react'
import ApplicationTable from '@/components/ApplicationTable'
import { applicationApi } from '@/services/api'
import { Application } from '@/types'

export default function ApplicationsPage() {
  const [applications, setApplications] = useState<Application[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const fetchApplications = async () => {
    try {
      setLoading(true)
      setError(null)
      const data = await applicationApi.list()
      setApplications(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load applications')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchApplications()
  }, [])

  const handleDelete = async (id: number) => {
    try {
      await applicationApi.delete(id)
      setApplications(applications.filter(app => app.id !== id))
    } catch (err) {
      alert(err instanceof Error ? err.message : 'Failed to delete application')
    }
  }

  return (
    <div>
      <h2>My Applications</h2>
      
      {error && (
        <div style={{ 
          color: '#721c24', 
          backgroundColor: '#f8d7da', 
          padding: '1rem', 
          borderRadius: '4px',
          marginBottom: '1rem'
        }}>
          Error: {error}
        </div>
      )}
      
      <ApplicationTable 
        applications={applications} 
        loading={loading}
        onDelete={handleDelete}
      />
    </div>
  )
}
