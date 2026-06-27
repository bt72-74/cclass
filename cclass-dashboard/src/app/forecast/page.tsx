'use client'

import { Layout } from '@/components/layout/Layout'
import { Card } from '@/components/ui/Card'
import { useForecast } from '@/hooks/useAPI'
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts'

export default function ForecastPage() {
  const { data, isLoading, error } = useForecast()

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
            پیش‌بینی فروش
          </h1>
          <p className="text-gray-600 mt-2">
            پیش‌بینی فروش برای 30 روز آینده
          </p>
        </div>

        {error && (
          <div className="p-4 bg-red-50 border border-red-200 rounded-lg text-red-600">
            خطا در بارگذاری پیش‌بینی
          </div>
        )}

        <Card title="نمودار پیش‌بینی" subtitle="30 روز آینده">
          <ResponsiveContainer width="100%" height={400}>
            <LineChart data={data?.forecast || []}>
              <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" />
              <XAxis dataKey="ds" />
              <YAxis />
              <Tooltip />
              <Legend />

              <Line
                type="monotone"
                dataKey="yhat"
                stroke="#3940AD"
                strokeWidth={3}
                dot={false}
                name="پیش‌بینی"
              />

              <Line
                type="monotone"
                dataKey="yhat_upper"
                stroke="#7C82D6"
                strokeDasharray="5 5"
                dot={false}
                name="حد بالا"
              />

              <Line
                type="monotone"
                dataKey="yhat_lower"
                stroke="#7C82D6"
                strokeDasharray="5 5"
                dot={false}
                name="حد پایین"
              />
            </LineChart>
          </ResponsiveContainer>
        </Card>
      </div>
    </Layout>
  )
}