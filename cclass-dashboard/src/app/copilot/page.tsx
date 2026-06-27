'use client'

import { useState, useRef, useEffect } from 'react'
import { Layout } from '@/components/layout/Layout'
import { Card } from '@/components/ui/Card'
import { useCopilotChat } from '@/hooks/useAPI'
import { Bot, Send, User, Loader2 } from 'lucide-react'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

const QUICK_PROMPTS = [
  'وضعیت فروش امروز چطوره؟',
  'سودآورترین محصولات کدامند؟',
  'پیش‌بینی فروش هفته آینده',
  'هشدارهای مهم امروز',
  'چطور می‌تونم فروش رو افزایش بدم؟',
]

export default function CopilotPage() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: 'assistant',
      content: 'سلام! من دستیار هوشمند شما هستم 🤖\n\nمی‌تونم داده‌های فروش، مشتریان و عملکرد کسب‌وکارتون رو تحلیل کنم و به هر سوالی پاسخ بدم.',
    },
  ])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const { sendMessage } = useCopilotChat()

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const handleSend = async (text?: string) => {
    const msg = text || input.trim()
    if (!msg || isLoading) return

    setInput('')
    setMessages((prev) => [...prev, { role: 'user', content: msg }])
    setIsLoading(true)

    let answer = ''
    try {
      const result = await sendMessage(msg)
      answer =
        result?.answer ||
        result?.agent_output?.analysis ||
        result?.llm_analysis ||
        '⚠️ پاسخی دریافت نشد.'
    } catch (err: any) {
      const status = err?.response?.status
      const detail = err?.response?.data?.detail
      if (status === 422) {
        answer = '⚠️ فرمت درخواست اشتباه است.'
      } else if (status === 500) {
        answer = `❌ خطای سرور: ${detail || 'لطفاً لاگ بک‌اند را بررسی کنید.'}`
      } else if (err?.code === 'ECONNREFUSED' || err?.code === 'ERR_NETWORK') {
        answer = '🔌 بک‌اند در دسترس نیست. سرور رو چک کنید.'
      } else {
        answer = `❌ خطا: ${err?.message || 'ارتباط با سرور برقرار نشد.'}`
      }
    } finally {
      setIsLoading(false)
      setMessages((prev) => [...prev, { role: 'assistant', content: answer }])
    }
  }

  return (
    <Layout>
      <div className="space-y-4 max-w-4xl mx-auto">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">دستیار هوش مصنوعی</h1>
          <p className="text-gray-600 mt-2">تحلیل هوشمند کسب‌وکار — هر سوالی دارید بپرسید</p>
        </div>

        <div className="flex flex-wrap gap-2">
          {QUICK_PROMPTS.map((p) => (
            <button
              key={p}
              onClick={() => handleSend(p)}
              disabled={isLoading}
              className="text-sm px-3 py-1.5 rounded-full border border-[#3940AD] text-[#3940AD] hover:bg-[#3940AD] hover:text-white transition-colors disabled:opacity-50"
            >
              {p}
            </button>
          ))}
        </div>

        <Card>
          <div className="h-[520px] overflow-y-auto space-y-4 p-2" dir="rtl">
            {messages.map((msg, i) => (
              <div key={i} className={`flex items-start gap-3 ${msg.role === 'user' ? 'flex-row-reverse' : ''}`}>
                <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${msg.role === 'assistant' ? 'bg-[#3940AD]' : 'bg-gray-200'}`}>
                  {msg.role === 'assistant'
                    ? <Bot size={16} className="text-white" />
                    : <User size={16} className="text-gray-600" />}
                </div>
                <div className={`max-w-[78%] rounded-2xl px-4 py-3 text-sm whitespace-pre-wrap leading-7 ${msg.role === 'assistant' ? 'bg-gray-100 text-gray-800' : 'bg-[#3940AD] text-white'}`}>
                  {msg.content}
                </div>
              </div>
            ))}

            {isLoading && (
              <div className="flex items-start gap-3">
                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-[#3940AD] flex items-center justify-center">
                  <Bot size={16} className="text-white" />
                </div>
                <div className="bg-gray-100 rounded-2xl px-4 py-3 flex items-center gap-2">
                  <Loader2 size={16} className="animate-spin text-[#3940AD]" />
                  <span className="text-xs text-gray-500">در حال پردازش...</span>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <div className="border-t border-gray-200 pt-4 mt-4" dir="rtl">
            <div className="flex gap-2">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && !e.shiftKey && handleSend()}
                placeholder="هر سوالی دارید بپرسید..."
                disabled={isLoading}
                className="flex-1 border border-gray-300 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-[#3940AD] disabled:opacity-50"
              />
              <button
                onClick={() => handleSend()}
                disabled={isLoading || !input.trim()}
                className="bg-[#3940AD] text-white rounded-lg px-4 py-2 hover:bg-[#2d3290] transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <Send size={16} />
              </button>
            </div>
          </div>
        </Card>
      </div>
    </Layout>
  )
}
