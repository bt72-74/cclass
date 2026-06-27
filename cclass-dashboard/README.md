# C Class Dashboard

داشبورد تحلیل فروش شرکت سی کلاس

## ویژگی‌ها

- 📊 داشبورد تحلیلی با KPI و نمودارها
- 📈 پیش‌بینی فروش با ML
- 🎯 فرصت‌های فروش هوشمند
- ⚠️ سیستم هشدارها
- 🔐 احراز هویت امن
- 🎨 UI حرفه‌ای با هویت بصری سی کلاس

## پشته فناوری

- **Frontend**: Next.js 14 + TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Zustand + Redux Toolkit
- **API**: TanStack Query + Axios
- **Charts**: Recharts
- **Icons**: Lucide Icons

## نصب و راه‌اندازی

```bash
# نصب وابستگی‌ها
npm install

# راه‌اندازی سرور توسعه
npm run dev

# ساختن برای production
npm run build
npm start
```

سرور در `http://localhost:3000` اجرا می‌شود.

## متغیرهای محیط

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

## ساختار پروژه

```
src/
├── app/           # صفحات و layout
├── components/    # components
│   ├── ui/       # UI components
│   └── layout/   # layout components
├── hooks/        # custom hooks (API hooks)
├── lib/          # utilities و API client
├── store/        # Redux و Zustand stores
└── public/       # static assets
```

## صفحات

- `/login` - صفحه ورود
- `/dashboard` - داشبورد اصلی
- `/forecast` - پیش‌بینی فروش
- `/opportunities` - فرصت‌های فروش
- `/alerts` - هشدارها
