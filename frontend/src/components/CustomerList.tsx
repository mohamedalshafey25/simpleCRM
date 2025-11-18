import React from 'react'
import { useCustomers } from '../api/customers'

export default function CustomerList() {
  // Start with automatic fetching disabled so the Load button triggers the fetch.
  const { data: customers, isLoading, isError, refetch } = useCustomers({ enabled: false })

  return (
    <div className="bg-white p-4 rounded shadow">
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-semibold mb-2">Customers</h2>
        <button
          className="text-sm bg-blue-500 text-white px-3 py-1 rounded"
          onClick={() => refetch()}
          disabled={isLoading}
        >
          {isLoading ? 'Loading...' : 'Load Customers'}
        </button>
      </div>
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
