import React from 'react'
import CustomersPage from './pages/Customers/CustomersPage'

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow p-4">
        <h1 className="text-xl font-bold">Simple CRM</h1>
      </header>
      <main className="p-4">
        <CustomersPage />
      </main>
    </div>
  )
}
