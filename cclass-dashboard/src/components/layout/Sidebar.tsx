import React from 'react'
import Link from 'next/link'
import { usePathname } from 'next/navigation'
import {
  BarChart3,
  TrendingUp,
  AlertCircle,
  Target,
  Settings,
  UserCheck,
  Package,
  Bot,
} from 'lucide-react'
import { useUIStore } from '@/store/ui'

const menuItems = [
  { href: '/dashboard', label: 'داشبورد', icon: BarChart3 },
  { href: '/copilot', label: 'دستیار هوشمند', icon: Bot },
  { href: '/products', label: 'محصولات', icon: Package },
  { href: '/salespersons', label: 'فروشندگان', icon: UserCheck },
  { href: '/forecast', label: 'پیش‌بینی', icon: TrendingUp },
  { href: '/opportunities', label: 'فرصت‌ها', icon: Target },
  { href: '/alerts', label: 'هشدارها', icon: AlertCircle },
  { href: '/settings', label: 'تنظیمات', icon: Settings },
]

export const Sidebar: React.FC = () => {
  const pathname = usePathname()
  const { sidebarOpen } = useUIStore()

  return (
    <aside
      className={`
        bg-white border-l border-gray-200 transition-all duration-300
        ${sidebarOpen ? 'w-64' : 'w-20'}
        fixed h-screen left-0 top-16 overflow-y-auto z-40
      `}
    >
      <nav className="p-4 space-y-2">
        {menuItems.map((item) => {
          const Icon = item.icon
          const isActive = pathname === item.href

          return (
            <Link
              key={item.href}
              href={item.href}
              className={`
                flex items-center gap-3 px-4 py-3 rounded-lg transition-colors
                ${isActive
                  ? 'bg-blue-50 text-[#3940AD] font-medium'
                  : 'text-gray-700 hover:bg-gray-50'
                }
              `}
            >
              <Icon size={20} className="flex-shrink-0" />
              {sidebarOpen && <span>{item.label}</span>}
            </Link>
          )
        })}
      </nav>
    </aside>
  )
}
