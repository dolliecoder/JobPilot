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
  location: string
  job_type: string
  description: string
  requirements?: string
  created_at: string
}

export interface Application {
  id: number
  resume_id: number
  job_id: number
  status: string
  applied_at: string
  job_title?: string
  job_company?: string
  resume_filename?: string
}
