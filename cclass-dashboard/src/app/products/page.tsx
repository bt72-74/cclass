'use client'

import { useState, useMemo } from 'react'
import { Layout } from '@/components/layout/Layout'
import { Card } from '@/components/ui/Card'
import { useProducts, useCategories, Product } from '@/hooks/useAPI'
import { Package, Search, ChevronDown, ChevronUp, Tag } from 'lucide-react'

export default function ProductsPage() {
  const { data: products, isLoading: loadingProducts } = useProducts()
  const { data: categories, isLoading: loadingCategories } = useCategories()
  const [search, setSearch] = useState('')
  const [openCategories, setOpenCategories] = useState<Set<number>>(new Set())
  const [showAll, setShowAll] = useState(false)

  const isLoading = loadingProducts || loadingCategories

  // Build category map id -> name
  const categoryMap = useMemo(() => {
    const map: Record<number, string> = {}
    categories?.forEach((c) => { map[c.id] = c.name })
    return map
  }, [categories])

  // Filter products by search
  const filtered = useMemo(() => {
    if (!products) return []
    const q = search.trim().toLowerCase()
    if (!q) return products
    return products.filter(
      (p) =>
        p.name.toLowerCase().includes(q) ||
        p.code.toLowerCase().includes(q) ||
        (categoryMap[p.category_id] || '').toLowerCase().includes(q)
    )
  }, [products, search, categoryMap])

  // Group by category
  const grouped = useMemo(() => {
    const map: Record<number, { catName: string; items: Product[] }> = {}
    filtered.forEach((p) => {
      if (!map[p.category_id]) {
        map[p.category_id] = { catName: categoryMap[p.category_id] || 'سایر', items: [] }
      }
      map[p.category_id].items.push(p)
    })
    // Sort categories by number of products desc
    return Object.entries(map)
      .sort((a, b) => b[1].items.length - a[1].items.length)
      .map(([catId, val]) => ({ catId: Number(catId), ...val }))
  }, [filtered, categoryMap])

  const toggleCategory = (catId: number) => {
    setOpenCategories((prev) => {
      const next = new Set(prev)
      if (next.has(catId)) next.delete(catId)
      else next.add(catId)
      return next
    })
  }

  const expandAll = () => {
    setOpenCategories(new Set(grouped.map((g) => g.catId)))
    setShowAll(true)
  }

  const collapseAll = () => {
    setOpenCategories(new Set())
    setShowAll(false)
  }

  if (isLoading) {
    return (
      <Layout>
        <div className="flex items-center justify-center min-h-screen">
          <div className="flex flex-col items-center gap-3">
            <div className="w-10 h-10 border-4 border-[#0074C2] border-t-transparent rounded-full animate-spin" />
            <p className="text-gray-500">در حال بارگذاری محصولات...</p>
          </div>
        </div>
      </Layout>
    )
  }

  return (
    <Layout>
      <div className="space-y-6" dir="rtl">
        {/* Header */}
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">محصولات</h1>
            <p className="text-gray-500 mt-1">
              {products?.length?.toLocaleString('fa-IR')} محصول در{' '}
              {grouped.length.toLocaleString('fa-IR')} دسته‌بندی
            </p>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={showAll ? collapseAll : expandAll}
              className="flex items-center gap-2 px-4 py-2 text-sm bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg transition-colors"
            >
              {showAll ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
              {showAll ? 'جمع کردن همه' : 'باز کردن همه'}
            </button>
          </div>
        </div>

        {/* Search Bar */}
        <div className="relative">
          <Search size={18} className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="جستجو بر اساس نام، کد یا دسته‌بندی..."
            className="w-full pr-10 pl-4 py-3 border border-gray-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-[#0074C2] bg-white shadow-sm"
          />
        </div>

        {/* Summary Cards */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="bg-white rounded-xl p-4 shadow-sm border border-gray-100 flex items-center gap-3">
            <div className="p-2 bg-blue-50 rounded-lg">
              <Package size={20} className="text-[#3940AD]" />
            </div>
            <div>
              <p className="text-xs text-gray-500">کل محصولات</p>
              <p className="text-xl font-bold text-gray-900">
                {products?.length.toLocaleString('fa-IR')}
              </p>
            </div>
          </div>
          <div className="bg-white rounded-xl p-4 shadow-sm border border-gray-100 flex items-center gap-3">
            <div className="p-2 bg-blue-50 rounded-lg">
              <Tag size={20} className="text-[#3940AD]" />
            </div>
            <div>
              <p className="text-xs text-gray-500">دسته‌بندی‌ها</p>
              <p className="text-xl font-bold text-gray-900">
                {grouped.length.toLocaleString('fa-IR')}
              </p>
            </div>
          </div>
          <div className="bg-white rounded-xl p-4 shadow-sm border border-gray-100 flex items-center gap-3">
            <div className="p-2 bg-blue-50 rounded-lg">
              <Package size={20} className="text-[#3940AD]" />
            </div>
            <div>
              <p className="text-xs text-gray-500">محصولات فعال</p>
              <p className="text-xl font-bold text-gray-900">
                {products?.filter((p) => p.is_active).length.toLocaleString('fa-IR')}
              </p>
            </div>
          </div>
          <div className="bg-white rounded-xl p-4 shadow-sm border border-gray-100 flex items-center gap-3">
            <div className="p-2 bg-blue-50 rounded-lg">
              <Package size={20} className="text-[#3940AD]" />
            </div>
            <div>
              <p className="text-xs text-gray-500">نتایج جستجو</p>
              <p className="text-xl font-bold text-gray-900">
                {filtered.length.toLocaleString('fa-IR')}
              </p>
            </div>
          </div>
        </div>

        {/* Category Groups */}
        {grouped.length === 0 ? (
          <div className="text-center py-16 text-gray-400">
            <Package size={48} className="mx-auto mb-3 opacity-30" />
            <p>محصولی یافت نشد</p>
          </div>
        ) : (
          <div className="space-y-3">
            {grouped.map(({ catId, catName, items }) => {
              const isOpen = openCategories.has(catId)
              return (
                <div
                  key={catId}
                  className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden"
                >
                  {/* Category Header */}
                  <button
                    onClick={() => toggleCategory(catId)}
                    className="w-full flex items-center justify-between px-5 py-4 hover:bg-gray-50 transition-colors"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 bg-blue-50 rounded-lg flex items-center justify-center">
                        <Tag size={15} className="text-[#3940AD]" />
                      </div>
                      <div className="text-right">
                        <span className="font-semibold text-gray-900">{catName}</span>
                        <span className="mr-2 text-xs text-gray-400">
                          ({items.length.toLocaleString('fa-IR')} محصول)
                        </span>
                      </div>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="text-xs bg-blue-50 text-[#0074C2] px-2 py-1 rounded-full font-medium">
                        {items.length}
                      </span>
                      {isOpen ? (
                        <ChevronUp size={18} className="text-gray-400" />
                      ) : (
                        <ChevronDown size={18} className="text-gray-400" />
                      )}
                    </div>
                  </button>

                  {/* Products Table */}
                  {isOpen && (
                    <div className="border-t border-gray-100">
                      <div className="overflow-x-auto">
                        <table className="w-full text-sm">
                          <thead className="bg-gray-50">
                            <tr>
                              <th className="text-right px-5 py-3 text-xs font-semibold text-gray-500">#</th>
                              <th className="text-right px-5 py-3 text-xs font-semibold text-gray-500">کد</th>
                              <th className="text-right px-5 py-3 text-xs font-semibold text-gray-500">نام محصول</th>
                              <th className="text-right px-5 py-3 text-xs font-semibold text-gray-500">قیمت خرید</th>
                              <th className="text-right px-5 py-3 text-xs font-semibold text-gray-500">قیمت فروش</th>
                              <th className="text-right px-5 py-3 text-xs font-semibold text-gray-500">حاشیه سود</th>
                              <th className="text-right px-5 py-3 text-xs font-semibold text-gray-500">وضعیت</th>
                            </tr>
                          </thead>
                          <tbody>
                            {items.map((product, idx) => (
                              <tr
                                key={product.id}
                                className="border-t border-gray-50 hover:bg-blue-50/30 transition-colors"
                              >
                                <td className="px-5 py-3 text-gray-400 text-xs">{idx + 1}</td>
                                <td className="px-5 py-3 font-mono text-gray-500 text-xs">{product.code}</td>
                                <td className="px-5 py-3 text-gray-800 font-medium max-w-xs">
                                  {product.name}
                                </td>
                                <td className="px-5 py-3 text-gray-600">
                                  {product.cost_price > 0
                                    ? product.cost_price.toLocaleString('fa-IR')
                                    : '—'}
                                </td>
                                <td className="px-5 py-3 text-blue-700 font-medium">
                                  {product.sale_price > 0
                                    ? product.sale_price.toLocaleString('fa-IR')
                                    : '—'}
                                </td>
                                <td className="px-5 py-3">
                                  {product.margin_percent > 0 ? (
                                    <div className="flex items-center gap-2">
                                      <div className="w-16 bg-gray-100 rounded-full h-1.5">
                                        <div
                                          className="bg-[#0074C2] h-1.5 rounded-full"
                                          style={{ width: `${Math.min(product.margin_percent, 100)}%` }}
                                        />
                                      </div>
                                      <span className="text-xs text-gray-600">
                                        {product.margin_percent.toFixed(1)}%
                                      </span>
                                    </div>
                                  ) : (
                                    <span className="text-gray-300 text-xs">—</span>
                                  )}
                                </td>
                                <td className="px-5 py-3">
                                  <span
                                    className={`text-xs px-2 py-1 rounded-full font-medium ${
                                      product.is_active
                                        ? 'bg-green-50 text-green-600'
                                        : 'bg-red-50 text-red-500'
                                    }`}
                                  >
                                    {product.is_active ? 'فعال' : 'غیرفعال'}
                                  </span>
                                </td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  )}
                </div>
              )
            })}
          </div>
        )}
      </div>
    </Layout>
  )
}
