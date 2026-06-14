// Type definitions for the application

export interface Resume {
  id: number
  filename: string
  file_path: string
  extracted_text?: string
  uploaded_at: string
}

export interface Job {
  id: number
  title: string
  company: string
  description: string
  requirements?: string
  location?: string
  created_at: string
}

export interface Application {
  id: number
  resume_id: number
  job_id: number
  match_score?: number
  status: 'pending' | 'applied' | 'rejected'
  applied_at: string
}
