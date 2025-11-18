import React from 'react'
import { useCreateCustomer } from '../api/customers'
import { useForm } from 'react-hook-form'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'
import { toast } from 'react-toastify'

const schema = z.object({
  name: z.string().min(1, 'Name is required'),
  email: z.string().email('Invalid email')
})

type FormData = z.infer<typeof schema>

export default function CustomerForm() {
  const mutation = useCreateCustomer()

  const {
    register,
    handleSubmit,
    formState: { errors },
    reset
  } = useForm<FormData>({ resolver: zodResolver(schema) })

  function onSubmit(data: FormData) {
    mutation.mutate(data, {
      onSuccess() {
        toast.success('Customer created', { autoClose: 3000 })
        reset()
      },
      onError(error: any) {
        const detail = error?.response?.data?.detail
        toast.error(detail || 'Error creating customer', { autoClose: 8000 })
      }
    })
  }

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-lg font-semibold mb-2">Create Customer</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <label className="block mb-2">
          <span className="text-sm">Name</span>
          <input className="mt-1 block w-full border rounded p-2" {...register('name')} />
          {errors.name && <p className="text-red-600 text-sm mt-1">{String(errors.name.message)}</p>}
        </label>
        <label className="block mb-2">
          <span className="text-sm">Email</span>
          <input className="mt-1 block w-full border rounded p-2" {...register('email')} />
          {errors.email && <p className="text-red-600 text-sm mt-1">{String(errors.email.message)}</p>}
        </label>
        <button className="bg-blue-600 text-white px-4 py-2 rounded" type="submit" disabled={mutation.isLoading}>
          {mutation.isLoading ? 'Creating...' : 'Create'}
        </button>
      </form>
    </div>
  )
}
