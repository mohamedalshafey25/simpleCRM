import React from 'react'
import { useCreateCustomer } from '../api/customers'

export default function CustomerForm() {
  const [name, setName] = React.useState('')
  const [email, setEmail] = React.useState('')
  const [message, setMessage] = React.useState<string | null>(null)

  const mutation = useCreateCustomer()

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setMessage(null)
    mutation.mutate(
      { name, email },
      {
        onSuccess() {
          setMessage('Customer created')
          setName('')
          setEmail('')
        },
        onError(error: any) {
          const detail = error?.response?.data?.detail
          setMessage(detail || 'Error creating customer')
        }
      }
    )
  }

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-lg font-semibold mb-2">Create Customer</h2>
      <form onSubmit={handleSubmit}>
        <label className="block mb-2">
          <span className="text-sm">Name</span>
          <input className="mt-1 block w-full border rounded p-2" value={name} onChange={(e) => setName(e.target.value)} />
        </label>
        <label className="block mb-2">
          <span className="text-sm">Email</span>
          <input className="mt-1 block w-full border rounded p-2" value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        <button className="bg-blue-600 text-white px-4 py-2 rounded" type="submit" disabled={mutation.isLoading}>
          {mutation.isLoading ? 'Creating...' : 'Create'}
        </button>
      </form>
      {message && <div className="mt-2 text-sm">{message}</div>}
    </div>
  )
}
