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

export function useCustomers() {
  return useQuery(['customers'], fetchCustomers)
}

export function useCreateCustomer() {
  const qc = useQueryClient()
  return useMutation(postCustomer, {
    onSuccess() {
      qc.invalidateQueries(['customers'])
    }
  })
}
