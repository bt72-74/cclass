'use client'

import { Layout } from '@/components/layout/Layout'
import { Card } from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'
import { User, Mail, Phone, MapPin } from 'lucide-react'

export default function ProfilePage() {
  const user = {
    name: 'محمد رضایی',
    email: 'user@cclass.ir',
    phone: '09121234567',
    city: 'تهران',
    role: 'مدیر فروش',
    joinDate: '1402/01/15',
  }

  return (
    <Layout>
      <div className="space-y-6">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">پروفایل کاربری</h1>
          <p className="text-gray-600 mt-2">اطلاعات حساب کاربری خود</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Avatar Card */}
          <Card className="lg:col-span-1">
            <div className="flex flex-col items-center text-center">
              <div className="w-24 h-24 bg-gradient-to-br from-[#3940AD] to-[#2F3596] rounded-full flex items-center justify-center mb-4">
                <User size={48} className="text-white" />
              </div>

              <h2 className="text-2xl font-bold text-gray-900">
                {user.name}
              </h2>

              <p className="text-[#3940AD] font-medium mt-2">
                {user.role}
              </p>

              <p className="text-sm text-gray-500 mt-4">
                عضو از {user.joinDate}
              </p>
            </div>
          </Card>

          {/* Info Card */}
          <Card className="lg:col-span-2" title="اطلاعات تماس">
            <div className="space-y-4">
              <div className="flex items-center gap-3 pb-4 border-b border-gray-200">
                <Mail size={20} className="text-[#3940AD]" />
                <div>
                  <p className="text-sm text-gray-600">ایمیل</p>
                  <p className="font-medium text-gray-900">{user.email}</p>
                </div>
              </div>

              <div className="flex items-center gap-3 pb-4 border-b border-gray-200">
                <Phone size={20} className="text-[#3940AD]" />
                <div>
                  <p className="text-sm text-gray-600">تلفن</p>
                  <p className="font-medium text-gray-900">{user.phone}</p>
                </div>
              </div>

              <div className="flex items-center gap-3">
                <MapPin size={20} className="text-[#3940AD]" />
                <div>
                  <p className="text-sm text-gray-600">شهر</p>
                  <p className="font-medium text-gray-900">{user.city}</p>
                </div>
              </div>
            </div>
          </Card>
        </div>

        {/* Activity Card */}
        <Card title="فعالیت اخیر">
          <div className="space-y-3">
            <div className="flex items-center justify-between pb-3 border-b border-gray-200">
              <p className="text-gray-600">آخرین ورود</p>
              <p className="font-medium text-gray-900">
                امروز ساعت 09:30
              </p>
            </div>

            <div className="flex items-center justify-between pb-3 border-b border-gray-200">
              <p className="text-gray-600">تغییر رمز عبور</p>
              <p className="font-medium text-gray-900">
                3 روز پیش
              </p>
            </div>

            <div className="flex items-center justify-between">
              <p className="text-gray-600">تغییر اطلاعات</p>
              <p className="font-medium text-gray-900">
                1 ماه پیش
              </p>
            </div>
          </div>
        </Card>

        {/* Actions */}
        <div className="flex gap-4">
          <Button
            className="bg-[#3940AD] hover:bg-[#2F3596] text-white border-none"
          >
            ویرایش پروفایل
          </Button>

          <Button
            className="bg-[#3940AD]/10 text-[#3940AD] hover:bg-[#3940AD]/20 border border-[#3940AD]/20"
          >
            تغییر رمز عبور
          </Button>
        </div>
      </div>
    </Layout>
  )
}