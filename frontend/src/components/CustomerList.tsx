import React from 'react'
import { useCustomers } from '../api/customers'

export default function CustomerList() {
  const { data: customers, isLoading, isError } = useCustomers()

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-lg font-semibold mb-2">Customers</h2>
      {isLoading && <div>Loading...</div>}
      {isError && <div className="text-red-600">Failed to load customers</div>}
      {!isLoading && customers && customers.length === 0 && <div>No customers</div>}
      {!isLoading && customers && (
        <ul>
          {customers.map((c) => (
            <li key={c.id} className="border-b py-2">
              <div className="font-medium">{c.name}</div>
              <div className="text-sm text-gray-600">{c.email}</div>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}
