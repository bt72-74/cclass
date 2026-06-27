'use client'

import { Layout } from '@/components/layout/Layout'
import { Card } from '@/components/ui/Card'
import { useOpportunities } from '@/hooks/useAPI'
import { Target, TrendingUp, User } from 'lucide-react'

export default function OpportunitiesPage() {
  const { data, isLoading, error } = useOpportunities()

  if (isLoading) {
    return (
      <Layout>
        <div className="flex items-center justify-center min-h-screen">
          <p className="text-lg text-gray-600">درحال بارگذاری...</p>
        </div>
      </Layout>
    )
  }

  return (
    <Layout>
      <div className="space-y-6">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">
            فرصت‌های فروش
          </h1>
          <p className="text-gray-600 mt-2">
            فرصت‌های فروش بر اساس تحلیل هوشمند
          </p>
        </div>

        {error && (
          <div className="p-4 bg-red-50 border border-red-200 rounded-lg text-red-600">
            خطا در بارگذاری فرصت‌ها
          </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Repurchase Opportunities */}
          <Card
            title="فرصت‌های بازخرید"
            subtitle="مشتریانی که برای بازخرید آماده‌اند"
          >
            <div className="space-y-3">
              <div className="flex items-start gap-3 p-3 bg-[#3940AD]/10 rounded-lg border border-[#3940AD]/20">
                <User size={20} className="text-[#3940AD] mt-1" />
                <div>
                  <p className="font-medium text-gray-900">محمد رضایی</p>
                  <p className="text-sm text-gray-600">
                    احتمال بازخرید: 85%
                  </p>
                </div>
              </div>

              <div className="flex items-start gap-3 p-3 bg-[#3940AD]/10 rounded-lg border border-[#3940AD]/20">
                <User size={20} className="text-[#3940AD] mt-1" />
                <div>
                  <p className="font-medium text-gray-900">سارا احمدی</p>
                  <p className="text-sm text-gray-600">
                    احتمال بازخرید: 78%
                  </p>
                </div>
              </div>
            </div>
          </Card>

          {/* Up-sell Opportunities */}
          <Card
            title="فرصت‌های ارتقاء فروش"
            subtitle="محصولات با قیمت بالاتر"
          >
            <div className="space-y-3">
              <div className="flex items-start gap-3 p-3 bg-[#3940AD]/10 rounded-lg border border-[#3940AD]/20">
                <TrendingUp size={20} className="text-[#3940AD] mt-1" />
                <div>
                  <p className="font-medium text-gray-900">محصول A</p>
                  <p className="text-sm text-gray-600">
                    فرصت ارتقاء: 45K تومان
                  </p>
                </div>
              </div>

              <div className="flex items-start gap-3 p-3 bg-[#3940AD]/10 rounded-lg border border-[#3940AD]/20">
                <TrendingUp size={20} className="text-[#3940AD] mt-1" />
                <div>
                  <p className="font-medium text-gray-900">محصول B</p>
                  <p className="text-sm text-gray-600">
                    فرصت ارتقاء: 32K تومان
                  </p>
                </div>
              </div>
            </div>
          </Card>

          {/* Cross-sell Opportunities */}
          <Card
            title="فرصت‌های فروش متقاطع"
            subtitle="محصولات مرتبط"
          >
            <div className="space-y-3">
              <div className="flex items-start gap-3 p-3 bg-[#3940AD]/10 rounded-lg border border-[#3940AD]/20">
                <Target size={20} className="text-[#3940AD] mt-1" />
                <div>
                  <p className="font-medium text-gray-900">پکیج X + Y</p>
                  <p className="text-sm text-gray-600">
                    درصد احتمال: 62%
                  </p>
                </div>
              </div>

              <div className="flex items-start gap-3 p-3 bg-[#3940AD]/10 rounded-lg border border-[#3940AD]/20">
                <Target size={20} className="text-[#3940AD] mt-1" />
                <div>
                  <p className="font-medium text-gray-900">پکیج Z + W</p>
                  <p className="text-sm text-gray-600">
                    درصد احتمال: 71%
                  </p>
                </div>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </Layout>
  )
}