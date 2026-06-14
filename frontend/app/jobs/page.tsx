import JobSearch from '@/components/JobSearch'
import JobTable from '@/components/JobTable'

export default function JobsPage() {
  return (
    <div>
      <h2>Job Listings</h2>
      <JobSearch />
      <JobTable />
    </div>
  )
}
