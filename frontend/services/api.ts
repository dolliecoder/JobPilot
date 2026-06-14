const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

// Resume API
export const resumeApi = {
  upload: async (file: File) => {
    // TODO: Implement resume upload
    console.log('Upload resume:', file.name)
  },
  
  list: async () => {
    // TODO: Implement resume listing
    return []
  },
  
  delete: async (id: number) => {
    // TODO: Implement resume deletion
    console.log('Delete resume:', id)
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
