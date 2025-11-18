import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import client from './client'

export type Customer = {
  id: number
  name: string
  email: string
}

async function fetchCustomers() {
  const res = await client.get('/customers/')
  return res.data as Customer[]
}

async function postCustomer(payload: { name: string; email: string }) {
  const res = await client.post('/customers/', payload)
  return res.data as Customer
}

export function useCustomers(options?: any) {
  return useQuery(['customers'], fetchCustomers, options)
}

export function useCreateCustomer() {
  const qc = useQueryClient()
  return useMutation(postCustomer, {
    // Optimistic update: add the new customer to cache immediately
    async onMutate(newCustomer) {
      await qc.cancelQueries(['customers'])
      const previous = qc.getQueryData<Customer[]>(['customers'])
      const optimisticCustomer: Customer = {
        id: Date.now(),
        name: newCustomer.name,
        email: newCustomer.email
      }
      qc.setQueryData(['customers'], (old: Customer[] | undefined) => (old ? [optimisticCustomer, ...old] : [optimisticCustomer]))
      return { previous }
    },
    onError(_err, _newCustomer, context: any) {
      // rollback
      if (context?.previous) {
        qc.setQueryData(['customers'], context.previous)
      }
    },
    onSettled() {
      qc.invalidateQueries(['customers'])
    }
  })
}
