'use client'

import { Layout } from '@/components/layout/Layout'
import { Card } from '@/components/ui/Card'
import { useAlerts } from '@/hooks/useAPI'
import { AlertCircle, CheckCircle, AlertTriangle, Info } from 'lucide-react'

const PRIMARY = '#3940AD'

export default function AlertsPage() {
  const { data, isLoading, error } = useAlerts()

  if (isLoading) {
    return (
      <Layout>
        <div className="flex items-center justify-center min-h-screen">
          <p className="text-lg text-gray-600">درحال بارگذاری...</p>
        </div>
      </Layout>
    )
  }

  const alerts = data?.alerts || []

  return (
    <Layout>
      <div className="space-y-6">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">هشدارها و اطلاعات</h1>
          <p className="text-gray-600 mt-2">هشدارهای سیستم و اطلاعات مهم</p>
        </div>

        {error && (
          <div className="p-4 bg-red-50 border border-red-200 rounded-lg text-red-600">
            خطا در بارگذاری هشدارها
          </div>
        )}

        {alerts.length === 0 ? (
          <Card>
            <div className="text-center py-12">
              <CheckCircle size={48} className={`text-[${PRIMARY}] mx-auto mb-4`} />
              <p className="text-gray-600 text-lg">هیچ هشداری وجود ندارد</p>
              <p className="text-gray-500 text-sm mt-2">همه چیز بخوبی پیش می‌رود</p>
            </div>
          </Card>
        ) : (
          <div className="space-y-4">
            {alerts.map((alert: any, index: number) => {
              const isError = alert.type === 'error'
              const isSuccess = alert.type === 'success'
              const isWarning = alert.type === 'warning'

              const Icon =
                alert.type === 'error'
                  ? AlertCircle
                  : alert.type === 'success'
                  ? CheckCircle
                  : alert.type === 'warning'
                  ? AlertTriangle
                  : Info

              return (
                <Card key={index}>
                  <div className="flex items-start gap-4">

                    {/* ICON WRAPPER */}
                    <div
                      className={`p-3 rounded-lg border ${
                        isError
                          ? 'bg-red-50 border-red-200'
                          : isSuccess
                          ? 'bg-green-50 border-green-200'
                          : isWarning
                          ? `bg-[${PRIMARY}]/10 border-[${PRIMARY}]/20`
                          : `bg-[${PRIMARY}]/10 border-[${PRIMARY}]/20`
                      }`}
                    >
                      <Icon
                        size={24}
                        className={
                          isError
                            ? 'text-red-600'
                            : isSuccess
                            ? 'text-green-600'
                            : `text-[${PRIMARY}]`
                        }
                      />
                    </div>

                    {/* CONTENT */}
                    <div className="flex-1">
                      <h3 className="font-semibold text-gray-900">
                        {alert.title}
                      </h3>
                      <p className="text-gray-600 text-sm mt-1">
                        {alert.message}
                      </p>
                      <p className="text-gray-500 text-xs mt-3">
                        {alert.timestamp}
                      </p>
                    </div>

                  </div>
                </Card>
              )
            })}
          </div>
        )}

        {/* SAMPLE ALERTS */}
        <div className="space-y-4">
          <h2 className="text-xl font-bold text-gray-900 mt-8">
            هشدارهای نمونه
          </h2>

          {/* WARNING SAMPLE */}
          <Card>
            <div className="flex items-start gap-4">
              <div className={`p-3 rounded-lg bg-[${PRIMARY}]/10 border border-[${PRIMARY}]/20`}>
                <AlertTriangle size={24} className={`text-[${PRIMARY}]`} />
              </div>
              <div className="flex-1">
                <h3 className="font-semibold text-gray-900">
                  فروش پایین‌تر از هدف
                </h3>
                <p className="text-gray-600 text-sm mt-1">
                  فروش امروز {Math.round(Math.random() * 30)}% پایین‌تر از هدف روزانه است
                </p>
              </div>
            </div>
          </Card>

          {/* ERROR SAMPLE */}
          <Card>
            <div className="flex items-start gap-4">
              <div className="p-3 rounded-lg bg-red-50 border border-red-200">
                <AlertCircle size={24} className="text-red-600" />
              </div>
              <div className="flex-1">
                <h3 className="font-semibold text-gray-900">
                  مشتریانی در خطر چرن
                </h3>
                <p className="text-gray-600 text-sm mt-1">
                  {Math.floor(Math.random() * 10)} مشتری احتمال چرن بالا دارند
                </p>
              </div>
            </div>
          </Card>

          {/* INFO SAMPLE */}
          <Card>
            <div className="flex items-start gap-4">
              <div className={`p-3 rounded-lg bg-[${PRIMARY}]/10 border border-[${PRIMARY}]/20`}>
                <Info size={24} className={`text-[${PRIMARY}]`} />
              </div>
              <div className="flex-1">
                <h3 className="font-semibold text-gray-900">
                  به‌روزرسانی داده‌های جدید
                </h3>
                <p className="text-gray-600 text-sm mt-1">
                  داده‌های فروش تا امروز بروز شده‌اند
                </p>
              </div>
            </div>
          </Card>

        </div>
      </div>
    </Layout>
  )
}