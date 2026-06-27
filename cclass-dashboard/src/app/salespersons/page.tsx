'use client'

import { useState } from 'react'
import { Layout } from '@/components/layout/Layout'
import { Card } from '@/components/ui/Card'
import { KPICard } from '@/components/ui/KPICard'
import { useSalespersonPerformance, SalesPersonPerformance } from '@/hooks/useAPI'
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  Cell,
} from 'recharts'
import { Users, TrendingUp, ShoppingCart, Award } from 'lucide-react'

const COLORS = ['#0074C2', '#22c55e', '#f97316', '#a855f7', '#ec4899', '#14b8a6']

function formatNumber(n: number): string {
  if (n >= 1_000_000_000) return (n / 1_000_000_000).toFixed(1) + ' م'
  if (n >= 1_000_000) return (n / 1_000_000).toFixed(1) + ' میل'
  if (n >= 1_000) return (n / 1_000).toFixed(0) + ' ه'
  return n.toLocaleString('fa-IR')
}

export default function SalespersonsPage() {
  const [startDate, setStartDate] = useState('')
  const [endDate, setEndDate] = useState('')
  const [appliedStart, setAppliedStart] = useState<string | undefined>()
  const [appliedEnd, setAppliedEnd] = useState<string | undefined>()

  const { data, isLoading, error } = useSalespersonPerformance(appliedStart, appliedEnd)

  const handleFilter = () => {
    setAppliedStart(startDate || undefined)
    setAppliedEnd(endDate || undefined)
  }

  const handleReset = () => {
    setStartDate('')
    setEndDate('')
    setAppliedStart(undefined)
    setAppliedEnd(undefined)
  }

  // محاسبه KPIها از داده‌ها
  const totalSales = data?.reduce((s, r) => s + r.total_sales, 0) ?? 0
  const totalProfit = data?.reduce((s, r) => s + r.total_profit, 0) ?? 0
  const totalInvoices = data?.reduce((s, r) => s + r.invoice_count, 0) ?? 0
  const avgMargin = data && data.length > 0
    ? data.reduce((s, r) => s + r.profit_margin_percent, 0) / data.length
    : 0

  // برترین فروشنده
  const sortedData = data ? [...data].sort((a, b) => b.total_sales - a.total_sales) : data

  // برترین فروشنده
  const topSeller = sortedData?.reduce<SalesPersonPerformance | null>(
    (best, r) => (!best || r.total_sales > best.total_sales ? r : best),
    null
  )

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
      <div className="space-y-6" dir="rtl">
        {/* Header */}
        <div>
          <h1 className="text-3xl font-bold text-gray-900">عملکرد فروشندگان</h1>
          <p className="text-gray-600 mt-2">گزارش مقدار فروش و سوددهی هر کارشناس فروش</p>
        </div>

        {/* Filter Bar */}
        <Card>
          <div className="flex flex-wrap items-end gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">از تاریخ</label>
              <input
                type="date"
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
                className="border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">تا تاریخ</label>
              <input
                type="date"
                value={endDate}
                onChange={(e) => setEndDate(e.target.value)}
                className="border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <button
              onClick={handleFilter}
              className="bg-[#3940AD] text-white px-5 py-2 rounded-lg text-sm font-medium hover:bg-[#2f3596] transition-colors"
            >
              اعمال فیلتر
            </button>
            {(appliedStart || appliedEnd) && (
              <button
                onClick={handleReset}
                className="bg-gray-100 text-gray-700 px-5 py-2 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors"
              >
                حذف فیلتر
              </button>
            )}
          </div>
        </Card>

        {/* KPI Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <KPICard
            title="مجموع فروش"
            value={formatNumber(totalSales)}
            unit="تومان"
            icon={<ShoppingCart size={24} />}
            color="primary"
          />
          <KPICard
            title="مجموع سود"
            value={formatNumber(totalProfit)}
            unit="تومان"
            icon={<TrendingUp size={24} />}
            color="primary"
          />
          <KPICard
            title="تعداد فاکتور"
            value={totalInvoices.toLocaleString('fa-IR')}
            icon={<Users size={24} />}
            color="primary"
          />
          <KPICard
            title="میانگین حاشیه سود"
            value={avgMargin.toFixed(1)}
            unit="%"
            icon={<Award size={24} />}
            color="primary"
          />
        </div>

        {/* Charts Row */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Sales Chart */}
          <Card title="مقدار فروش هر فروشنده" subtitle="مجموع فروش (تومان)">
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={sortedData} margin={{ top: 5, right: 10, left: 10, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" tick={{ fontSize: 11 }} />
                <YAxis tickFormatter={(v) => formatNumber(v)} tick={{ fontSize: 11 }} />
                <Tooltip formatter={(v: number) => [v.toLocaleString('fa-IR') + ' تومان', 'فروش']} />
                <Bar dataKey="total_sales" name="مجموع فروش" radius={[4, 4, 0, 0]}>
                  {sortedData?.map((_, i) => (
                    <Cell key={i} fill={COLORS[i % COLORS.length]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </Card>

          {/* Profit Chart */}
          <Card title="مقدار سود هر فروشنده" subtitle="مجموع سود (تومان)">
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={sortedData} margin={{ top: 5, right: 10, left: 10, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" tick={{ fontSize: 11 }} />
                <YAxis tickFormatter={(v) => formatNumber(v)} tick={{ fontSize: 11 }} />
                <Tooltip formatter={(v: number) => [v.toLocaleString('fa-IR') + ' تومان', 'سود']} />
                <Bar dataKey="total_profit" name="مجموع سود" radius={[4, 4, 0, 0]}>
                  {sortedData?.map((_, i) => (
                    <Cell key={i} fill={COLORS[i % COLORS.length]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </Card>
        </div>

        {/* Profit Margin Chart */}
        <Card title="درصد حاشیه سود هر فروشنده" subtitle="سود / فروش × ۱۰۰">
          <ResponsiveContainer width="100%" height={250}>
            <BarChart data={sortedData} margin={{ top: 5, right: 10, left: 10, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" tick={{ fontSize: 11 }} />
              <YAxis unit="%" tick={{ fontSize: 11 }} />
              <Tooltip formatter={(v: number) => [v.toFixed(2) + '%', 'حاشیه سود']} />
              <Bar dataKey="profit_margin_percent" name="حاشیه سود %" radius={[4, 4, 0, 0]}>
                {sortedData?.map((_, i) => (
                  <Cell key={i} fill={COLORS[i % COLORS.length]} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </Card>

        {/* Table */}
        <Card title="جدول عملکرد فروشندگان" subtitle="مشاهده کامل اطلاعات">
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-gray-200 text-gray-600">
                  <th className="text-right py-3 px-4 font-semibold">ردیف</th>
                  <th className="text-right py-3 px-4 font-semibold">کد</th>
                  <th className="text-right py-3 px-4 font-semibold">نام فروشنده</th>
                  <th className="text-right py-3 px-4 font-semibold">تعداد فاکتور</th>
                  <th className="text-right py-3 px-4 font-semibold">مجموع فروش (تومان)</th>
                  <th className="text-right py-3 px-4 font-semibold">مجموع سود (تومان)</th>
                  <th className="text-right py-3 px-4 font-semibold">حاشیه سود</th>
                  <th className="text-right py-3 px-4 font-semibold">وضعیت</th>
                </tr>
              </thead>
              <tbody>
                {sortedData?.map((sp, index) => (
                  <tr
                    key={sp.id}
                    className={`border-b border-gray-100 hover:bg-gray-50 transition-colors ${
                      topSeller?.id === sp.id ? 'bg-yellow-50' : ''
                    }`}
                  >
                    <td className="py-3 px-4 text-gray-500">{index + 1}</td>
                    <td className="py-3 px-4 font-mono text-gray-600">{sp.code}</td>
                    <td className="py-3 px-4 font-medium text-gray-900">
                      {sp.name}
                      {topSeller?.id === sp.id && (
                        <span className="mr-2 text-xs bg-yellow-100 text-yellow-700 px-2 py-0.5 rounded-full">
                          🏆 برتر
                        </span>
                      )}
                    </td>
                    <td className="py-3 px-4 text-gray-700">
                      {sp.invoice_count.toLocaleString('fa-IR')}
                    </td>
                    <td className="py-3 px-4 text-blue-700 font-medium">
                      {sp.total_sales.toLocaleString('fa-IR')}
                    </td>
                    <td className="py-3 px-4 text-green-700 font-medium">
                      {sp.total_profit.toLocaleString('fa-IR')}
                    </td>
                    <td className="py-3 px-4">
                      <div className="flex items-center gap-2">
                        <div className="flex-1 bg-gray-200 rounded-full h-2 max-w-[80px]">
                          <div
                            className="bg-[#0074C2] h-2 rounded-full"
                            style={{ width: `${Math.min(sp.profit_margin_percent, 100)}%` }}
                          />
                        </div>
                        <span className="text-gray-700 text-xs font-medium w-12">
                          {sp.profit_margin_percent.toFixed(1)}%
                        </span>
                      </div>
                    </td>
                    <td className="py-3 px-4">
                      <span
                        className={`text-xs px-2 py-1 rounded-full font-medium ${
                          sp.is_active
                            ? 'bg-green-100 text-green-700'
                            : 'bg-red-100 text-red-600'
                        }`}
                      >
                        {sp.is_active ? 'فعال' : 'غیرفعال'}
                      </span>
                    </td>
                  </tr>
                ))}
                {(!data || data.length === 0) && (
                  <tr>
                    <td colSpan={8} className="text-center py-10 text-gray-400">
                      داده‌ای یافت نشد
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </Card>
      </div>
    </Layout>
  )
}
