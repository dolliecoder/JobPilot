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
  list: async () => {
    // TODO: Implement job listing
    return []
  },
  
  get: async (id: number) => {
    // TODO: Implement job retrieval
    return null
  },
  
  create: async (jobData: any) => {
    // TODO: Implement job creation
    console.log('Create job:', jobData)
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
