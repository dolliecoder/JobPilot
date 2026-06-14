'use client'

import { useState, useEffect } from 'react'
import JobSearch from '@/components/JobSearch'
import JobTable from '@/components/JobTable'
import ApplyModal from '@/components/ApplyModal'
import { jobApi } from '@/services/api'
import { Job } from '@/types'

export default function JobsPage() {
  const [jobs, setJobs] = useState<Job[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [selectedJob, setSelectedJob] = useState<Job | null>(null)

  const fetchJobs = async (keyword: string = '') => {
    try {
      setLoading(true)
      setError(null)
      const data = await jobApi.list(keyword)
      setJobs(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load jobs')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchJobs()
  }, [])

  const handleSearch = (keyword: string) => {
    fetchJobs(keyword)
  }

  const handleApply = (job: Job) => {
    setSelectedJob(job)
  }

  const handleCloseModal = () => {
    setSelectedJob(null)
  }

  return (
    <div>
      <h2>Job Listings</h2>
      <JobSearch onSearch={handleSearch} />
      
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
      
      <JobTable jobs={jobs} loading={loading} onApply={handleApply} />
      
      {selectedJob && (
        <ApplyModal job={selectedJob} onClose={handleCloseModal} />
      )}
    </div>
  )
}
