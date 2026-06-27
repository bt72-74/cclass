import React from 'react'
import { ArrowUp, ArrowDown } from 'lucide-react'

interface KPICardProps {
  title: string
  value: number | string
  unit?: string
  trend?: number
  icon?: React.ReactNode
  color?: 'blue' | 'green' | 'orange' | 'red' | 'primary'
}

const colorClasses = {
  blue: 'bg-blue-50 text-blue-600 border-blue-200',
  green: 'bg-green-50 text-green-600 border-green-200',
  orange: 'bg-orange-50 text-orange-600 border-orange-200',
  red: 'bg-red-50 text-red-600 border-red-200',
  primary: 'bg-[#3940AD]/10 text-[#3940AD] border-[#3940AD]/20',
}

export const KPICard: React.FC<KPICardProps> = ({
  title,
  value,
  unit,
  trend,
  icon,
  color = 'blue',
}) => {
  return (
    <div className={`rounded-lg p-6 border ${colorClasses[color]}`}>
      <div className="flex items-start justify-between">
        <div>
          <p className="text-sm font-medium text-gray-600 mb-2">{title}</p>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl font-bold">{value}</span>
            {unit && <span className="text-sm text-gray-600">{unit}</span>}
          </div>
          {trend !== undefined && (
            <div className={`flex items-center gap-1 mt-2 text-sm font-medium ${trend >= 0 ? 'text-green-600' : 'text-red-600'}`}>
              {trend >= 0 ? <ArrowUp size={16} /> : <ArrowDown size={16} />}
              <span>{Math.abs(trend)}%</span>
            </div>
          )}
        </div>
        {icon && <div className="text-3xl">{icon}</div>}
      </div>
    </div>
  )
}
