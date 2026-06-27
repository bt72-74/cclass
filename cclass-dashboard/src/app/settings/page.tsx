'use client'

import { Layout } from '@/components/layout/Layout'
import { Card } from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'
import { useThemeStore } from '@/store/theme'
import { Moon, Sun, Bell, Lock, Globe } from 'lucide-react'
import { useState } from 'react'

export default function SettingsPage() {
  const { darkMode, toggleDarkMode } = useThemeStore()
  const [notifications, setNotifications] = useState(true)
  const [language, setLanguage] = useState('fa')

  return (
    <Layout>
      <div className="space-y-6 max-w-2xl">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">تنظیمات</h1>
          <p className="text-gray-600 mt-2">تنظیمات برنامه و حساب کاربری</p>
        </div>

        {/* Display Settings */}
        <Card title="نمایش">
          <div className="space-y-4">
            <div className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div className="flex items-center gap-3">
                {darkMode ? <Moon size={20} className="text-gray-600" /> : <Sun size={20} className="text-gray-600" />}
                <div>
                  <p className="font-medium text-gray-900">حالت تاریک</p>
                  <p className="text-sm text-gray-600">تغییر بین روز و شب</p>
                </div>
              </div>
              <button
                onClick={toggleDarkMode}
                className={`w-12 h-6 rounded-full transition-colors ${
                  darkMode ? 'bg-[#0074C2]' : 'bg-gray-300'
                } relative`}
              >
                <div
                  className={`w-5 h-5 bg-white rounded-full absolute top-0.5 transition-transform ${
                    darkMode ? 'translate-x-6' : 'translate-x-0.5'
                  }`}
                />
              </button>
            </div>

            <div className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div className="flex items-center gap-3">
                <Globe size={20} className="text-gray-600" />
                <div>
                  <p className="font-medium text-gray-900">زبان</p>
                  <p className="text-sm text-gray-600">انتخاب زبان رابط</p>
                </div>
              </div>
              <select
                value={language}
                onChange={(e) => setLanguage(e.target.value)}
                className="px-3 py-2 border border-gray-300 rounded-lg bg-white"
              >
                <option value="fa">فارسی</option>
                <option value="en">English</option>
              </select>
            </div>
          </div>
        </Card>

        {/* Notification Settings */}
        <Card title="اطلاع‌رسانی">
          <div className="space-y-4">
            <div className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div className="flex items-center gap-3">
                <Bell size={20} className="text-gray-600" />
                <div>
                  <p className="font-medium text-gray-900">اطلاع‌رسانی‌های فروش</p>
                  <p className="text-sm text-gray-600">دریافت اطلاع‌رسانی درباره فروش جدید</p>
                </div>
              </div>
              <button
                onClick={() => setNotifications(!notifications)}
                className={`w-12 h-6 rounded-full transition-colors ${
                  notifications ? 'bg-[#0074C2]' : 'bg-gray-300'
                } relative`}
              >
                <div
                  className={`w-5 h-5 bg-white rounded-full absolute top-0.5 transition-transform ${
                    notifications ? 'translate-x-6' : 'translate-x-0.5'
                  }`}
                />
              </button>
            </div>
          </div>
        </Card>

        {/* Security Settings */}
        <Card title="امنیت">
          <div className="space-y-4">
            <div className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div className="flex items-center gap-3">
                <Lock size={20} className="text-gray-600" />
                <div>
                  <p className="font-medium text-gray-900">رمز عبور</p>
                  <p className="text-sm text-gray-600">تغییر رمز عبور حساب کاربری</p>
                </div>
              </div>
              <Button variant="secondary" size="sm">
                تغییر
              </Button>
            </div>
          </div>
        </Card>

        {/* Save Button */}
        <div className="flex gap-4">
          <Button variant="primary">ذخیره تنظیمات</Button>
          <Button variant="secondary">لغو</Button>
        </div>
      </div>
    </Layout>
  )
}
