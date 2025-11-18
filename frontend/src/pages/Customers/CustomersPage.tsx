import React from 'react'
import CustomerList from '../../components/CustomerList'
import CustomerForm from '../../components/CustomerForm'

export default function CustomersPage() {
  return (
    <div className="container mx-auto">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="md:col-span-2">
          <CustomerList />
        </div>
        <div>
          <CustomerForm />
        </div>
      </div>
    </div>
  )
}
