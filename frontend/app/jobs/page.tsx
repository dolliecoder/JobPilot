import { Suspense } from 'react'
import JobsClient from './JobsClient'

export default function Page() {
  return (
    <Suspense fallback={null}>
      <JobsClient />
    </Suspense>
  )
}
