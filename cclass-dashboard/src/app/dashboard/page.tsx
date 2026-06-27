'use client'

import { Layout } from '@/components/layout/Layout'
import { Card } from '@/components/ui/Card'
import { KPICard } from '@/components/ui/KPICard'
import { useDashboard } from '@/hooks/useAPI'
import { BarChart3, TrendingUp, Users, ShoppingCart } from 'lucide-react'
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

export default function DashboardPage() {
  const { data, isLoading, error } = useDashboard()

  if (isLoading) {
    return (
      <Layout>
        <div className="flex items-center justify-center min-h-screen">
          <p className="text-lg text-gray-600">درحال بارگذاری...</p>
        </div>
      </Layout>
    )
  }

  if (error) {
    return (
      <Layout>
        <div className="text-center py-12">
          <p className="text-red-600 text-lg">خطا در بارگذاری داده‌ها</p>
        </div>
      </Layout>
    )
  }

  return (
    <Layout>
      <div className="space-y-6">
        {/* Header */}
        <div>
          <h1 className="text-3xl font-bold text-gray-900">داشبورد</h1>
        </div>

        {/* KPI Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <KPICard
            title="فروش امروز"
            value={data?.sales_today || 0}
            unit="تومان"
            trend={data?.sales_growth_percent}
            icon={<ShoppingCart size={24} />}
            color="primary"
          />
          <KPICard
            title="فروش ماه"
            value={data?.sales_month || 0}
            unit="تومان"
            icon={<BarChart3 size={24} />}
            color="primary"
          />
          <KPICard
            title="سود امروز"
            value={data?.profit_today || 0}
            unit="تومان"
            icon={<TrendingUp size={24} />}
            color="primary"
          />
          <KPICard
            title="تحقق هدف"
            value={data?.sales_target_achievement_percent || 0}
            unit="%"
            icon={<Users size={24} />}
            color="primary"
          />
        </div>

        {/* Charts Row */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Daily Sales Trend */}
          <Card title="روند فروش روزانه" subtitle="فروش 7 روز اخیر">
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={data?.daily_sales_trend || []}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="amount"
                  stroke="#3940AD"
                  dot={{ fill: '#3940AD' }}
                  name="فروش"
                />
              </LineChart>
            </ResponsiveContainer>
          </Card>

          {/* Category Share */}
          <Card title="سهم دسته‌بندی‌ها" subtitle="توزیع فروش بر حسب دسته">
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={data?.category_share || []}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="sales" fill="#3940AD" name="فروش" />
              </BarChart>
            </ResponsiveContainer>
          </Card>
        </div>

        {/* Stats Row */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <Card>
            <div className="text-center">
              <p className="text-gray-600 text-sm mb-2">مشتریان فعال</p>
              <p className="text-3xl font-bold text-[#3940ad]">{data?.active_customers || 0}</p>
            </div>
          </Card>
          <Card>
            <div className="text-center">
              <p className="text-gray-600 text-sm mb-2">فاکتورهای صادر شده</p>
              <p className="text-3xl font-bold text-[#3940ad]">{data?.invoice_count || 0}</p>
            </div>
          </Card>
          <Card>
            <div className="text-center">
              <p className="text-gray-600 text-sm mb-2">متوسط فاکتور</p>
              <p className="text-3xl font-bold text-[#3940ad]">{data?.avg_invoice_amount || 0}</p>
            </div>
          </Card>
        </div>
      </div>
    </Layout>
  )
}
