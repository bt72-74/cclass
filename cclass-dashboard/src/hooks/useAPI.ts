import { useQuery } from '@tanstack/react-query'
import apiClient from '@/lib/api-client'

export interface DashboardSummary {
  sales_today: number
  sales_week: number
  sales_month: number
  sales_year: number
  profit_today: number
  profit_month: number
  active_customers: number
  new_customers: number
  invoice_count: number
  avg_invoice_amount: number
  sales_growth_percent: number
  profit_growth_percent: number
  sales_target_achievement_percent: number
  daily_sales_trend: any[]
  weekly_sales_trend: any[]
  monthly_sales_trend: any[]
  category_share: any[]
  salesperson_share: any[]
}

export interface SalesPersonPerformance {
  id: number
  code: string
  name: string
  phone: string | null
  email: string | null
  is_active: boolean
  total_sales: number
  total_profit: number
  invoice_count: number
  profit_margin_percent: number
}

export const useDashboard = () => {
  return useQuery<DashboardSummary>({
    queryKey: ['dashboard'],
    queryFn: async () => {
      const { data } = await apiClient.get('/dashboard/summary')
      return data
    },
    staleTime: 5 * 60 * 1000,
    refetchInterval: 10 * 60 * 1000,
  })
}

export const useSalespersonPerformance = (startDate?: string, endDate?: string) => {
  return useQuery<SalesPersonPerformance[]>({
    queryKey: ['salesperson-performance', startDate, endDate],
    queryFn: async () => {
      const params: Record<string, string> = {}
      if (startDate) params.start_date = startDate
      if (endDate) params.end_date = endDate
      const { data } = await apiClient.get('/salespersons/performance', { params })
      return data
    },
    staleTime: 5 * 60 * 1000,
  })
}

export const useSales = () => {
  return useQuery({
    queryKey: ['sales'],
    queryFn: async () => {
      const { data } = await apiClient.get('/sales')
      return data
    },
  })
}

export const useCustomers = () => {
  return useQuery({
    queryKey: ['customers'],
    queryFn: async () => {
      const { data } = await apiClient.get('/customers')
      return data
    },
  })
}

export const useForecast = () => {
  return useQuery({
    queryKey: ['forecast'],
    queryFn: async () => {
      const { data } = await apiClient.post('/copilot/chat', {
        message: 'پیش‌بینی فروش 30 روز آینده',
      })
      // Backend returns { agent_output: { type: "forecast", forecast: [...] } }
      return data?.agent_output ?? data
    },
  })
}

export const useOpportunities = () => {
  return useQuery({
    queryKey: ['opportunities'],
    queryFn: async () => {
      const { data } = await apiClient.post('/copilot/chat', {
        message: 'فرصت‌های فروش',
      })
      return data?.agent_output ?? data
    },
  })
}

export const useAlerts = () => {
  return useQuery({
    queryKey: ['alerts'],
    queryFn: async () => {
      const { data } = await apiClient.post('/copilot/chat', {
        message: 'هشدارهای امروز',
      })
      return data?.agent_output ?? data
    },
    refetchInterval: 5 * 60 * 1000,
  })
}

export const useCopilotChat = () => {
  const sendMessage = async (message: string, params?: Record<string, any>) => {
    const { data } = await apiClient.post('/copilot/chat', { message, params })
    return data
  }
  return { sendMessage }
}

export interface Category {
  id: number
  name: string
}

export interface Product {
  id: number
  code: string
  name: string
  category_id: number
  brand_id: number
  cost_price: number
  sale_price: number
  margin_percent: number
  is_active: boolean
}

export const useProducts = () => {
  return useQuery<Product[]>({
    queryKey: ['products'],
    queryFn: async () => {
      const { data } = await apiClient.get('/products/?limit=1000')
      return data
    },
    staleTime: 10 * 60 * 1000,
  })
}

export const useCategories = () => {
  return useQuery<Category[]>({
    queryKey: ['categories'],
    queryFn: async () => {
      const { data } = await apiClient.get('/categories/')
      return data
    },
    staleTime: 60 * 60 * 1000,
  })
}
