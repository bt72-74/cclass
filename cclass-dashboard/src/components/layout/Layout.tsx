import React from 'react'
import { Header } from './Header'
import { Sidebar } from './Sidebar'
import { useUIStore } from '@/store/ui'

interface LayoutProps {
  children: React.ReactNode
}

export const Layout: React.FC<LayoutProps> = ({ children }) => {
  const { sidebarOpen } = useUIStore()

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <Sidebar />
      <main
        className={`
          transition-all duration-300 pt-16
          ${sidebarOpen ? 'pl-64' : 'pl-20'}
          min-h-screen
        `}
      >
        <div className="p-6">{children}</div>
      </main>
    </div>
  )
}
