import { Resume } from '@/types'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

// Resume API
export const resumeApi = {
  upload: async (file: File): Promise<Resume> => {
    const formData = new FormData()
    formData.append('file', file)
    
    const response = await fetch(`${API_URL}/api/resumes/upload`, {
      method: 'POST',
      body: formData,
    })
    
    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.detail || 'Failed to upload resume')
    }
    
    return response.json()
  },
  
  list: async (): Promise<Resume[]> => {
    const response = await fetch(`${API_URL}/api/resumes/`)
    
    if (!response.ok) {
      throw new Error('Failed to fetch resumes')
    }
    
    const data = await response.json()
    return data.resumes
  },
  
  delete: async (id: number): Promise<void> => {
    const response = await fetch(`${API_URL}/api/resumes/${id}`, {
      method: 'DELETE',
    })
    
    if (!response.ok) {
      throw new Error('Failed to delete resume')
    }
  }
}

// Job API
export const jobApi = {
  list: async (keyword?: string): Promise<Job[]> => {
    const url = new URL(`${API_URL}/api/jobs/`)
    if (keyword) {
      url.searchParams.append('keyword', keyword)
    }
    
    const response = await fetch(url.toString())
    
    if (!response.ok) {
      throw new Error('Failed to fetch jobs')
    }
    
    const data = await response.json()
    return data.jobs
  },
  
  get: async (id: number): Promise<Job> => {
    const response = await fetch(`${API_URL}/api/jobs/${id}`)
    
    if (!response.ok) {
      throw new Error('Failed to fetch job')
    }
    
    return response.json()
  },
  
  create: async (jobData: Partial<Job>): Promise<Job> => {
    const response = await fetch(`${API_URL}/api/jobs/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(jobData),
    })
    
    if (!response.ok) {
      throw new Error('Failed to create job')
    }
    
    return response.json()
  }
}

// Application API
export const applicationApi = {
  list: async () => {
    // TODO: Implement application listing
    return []
  },
  
  create: async (resumeId: number, jobId: number) => {
    // TODO: Implement application creation
    console.log('Create application:', resumeId, jobId)
  },
  
  updateStatus: async (id: number, status: string) => {
    // TODO: Implement status update
    console.log('Update application status:', id, status)
  }
}
