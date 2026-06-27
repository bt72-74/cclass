import React from 'react'
import Link from 'next/link'
import Image from 'next/image'
import { Menu, LogOut, Moon, Sun, Settings, User } from 'lucide-react'
import { useUIStore } from '@/store/ui'
import { useThemeStore } from '@/store/theme'

export const Header: React.FC = () => {
  const { toggleSidebar } = useUIStore()
  const { darkMode, toggleDarkMode } = useThemeStore()

  const handleLogout = () => {
    localStorage.removeItem('token')
    window.location.href = '/login'
  }

  return (
    <header className="bg-gradient-to-r from-[#3941add2] to-[#3941ad] text-white  fixed top-0 left-0 right-0 z-50 h-16">
      <div className="flex items-center justify-between px-6 h-full">
        {/* Left Section */}
        <div className="flex items-center gap-4">
          <button
            onClick={toggleSidebar}
            className="p-2 hover:bg-white/10 rounded-lg transition-colors"
          >
            <Menu size={24} />
          </button>

          {/* Logo */}
          <div className="relative w-64 h-10">
            <Image
              src="/logo.png"
              alt="C.Class Logo"
              fill
              className="object-contain"
              priority
            />
          </div>
        </div>

        {/* Right Section */}
        <div className="flex items-center gap-3">
          <button
            onClick={toggleDarkMode}
            className="p-2 hover:bg-white/10 rounded-lg transition-colors"
            title={darkMode ? 'روز' : 'شب'}
          >
            {darkMode ? <Sun size={20} /> : <Moon size={20} />}
          </button>

          <Link
            href="/profile"
            className="p-2 hover:bg-white/10 rounded-lg transition-colors"
          >
            <User size={20} />
          </Link>

          <Link
            href="/settings"
            className="p-2 hover:bg-white/10 rounded-lg transition-colors"
          >
            <Settings size={20} />
          </Link>

          <button
            onClick={handleLogout}
            className="flex items-center gap-2 px-4 py-2 bg-white/20 hover:bg-white/30 rounded-lg transition-colors"
          >
            <LogOut size={20} />
            <span className="text-sm font-medium">خروج</span>
          </button>
        </div>
      </div>
    </header>
  )
}