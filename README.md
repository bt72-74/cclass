# C-Class BI Platform

سامانه هوش تجاری (Business Intelligence) مبتنی بر هوش مصنوعی برای تحلیل فروش، پیش‌بینی روند فروش و پشتیبانی از تصمیم‌گیری مدیران.

---

# معرفی پروژه

C-Class BI یک سامانه جامع هوش تجاری است که با هدف تحلیل داده‌های فروش، پایش شاخص‌های کلیدی عملکرد (KPI)، پیش‌بینی فروش و ارائه بینش‌های هوشمند به مدیران توسعه یافته است.

این پروژه با ترکیب تحلیل داده، مدل‌های یادگیری ماشین و مدل‌های زبانی بزرگ (LLM)، بستری برای تصمیم‌گیری هوشمند در سازمان‌ها فراهم می‌کند.

---

# قابلیت‌ها

## داشبورد مدیریتی

* نمایش شاخص‌های کلیدی عملکرد (KPI)
* گزارش‌های تحلیلی فروش
* نمودارهای تعاملی
* تحلیل عملکرد محصولات
* تحلیل مشتریان

## دستیار هوشمند (AI Copilot)

* پاسخ به پرسش‌های کاربران به زبان طبیعی
* تحلیل هوشمند داده‌های فروش
* تولید گزارش‌های مدیریتی
* ارائه پیشنهادهای مبتنی بر داده
* تحلیل زمینه‌ای اطلاعات

## پیش‌بینی فروش

* پیش‌بینی فروش با Prophet
* پیش‌بینی فروش با LSTM
* پیش‌بینی فروش با XGBoost
* تحلیل روند فروش
* پیش‌بینی عملکرد آینده

## تحلیل عملکرد فروشندگان

* رتبه‌بندی فروشندگان
* ارزیابی عملکرد
* محاسبه شاخص‌های عملکرد
* مقایسه عملکرد افراد
* گزارش‌های مدیریتی

## تحلیل محصولات

* شناسایی محصولات پرفروش
* تحلیل سودآوری محصولات
* تحلیل برندها
* تحلیل دسته‌بندی کالاها
* شناسایی محصولات کم‌گردش

## تحلیل مشتریان

* بخش‌بندی مشتریان
* تحلیل RFM
* تحلیل رفتار خرید
* پیش‌بینی خرید مجدد
* ارزش طول عمر مشتری (CLV)

## موتور پیشنهاد فروش

* پیشنهاد فروش مکمل (Cross Selling)
* پیشنهاد فروش ارتقایی (Up Selling)
* تحلیل فرصت‌های فروش
* سیستم پیشنهاددهنده
* تحلیل شباهت محصولات و مشتریان

## سیستم هشدار

* تشخیص افت فروش
* شناسایی ناهنجاری‌ها
* هشدارهای مدیریتی
* پیشنهاد اقدامات اصلاحی

---

# معماری سیستم

```
               Next.js Dashboard
                       │
                REST API + JWT
                       │
        ┌───────────────────────────────┐
        │        FastAPI Backend         │
        ├───────────────────────────────┤
        │ احراز هویت                     │
        │ داشبورد مدیریتی                │
        │ دستیار هوشمند                 │
        │ تحلیل فروش                    │
        │ پیش‌بینی فروش                 │
        │ تحلیل مشتریان                 │
        │ تحلیل محصولات                 │
        │ موتور پیشنهاد فروش            │
        └───────────────────────────────┘
                       │
                 PostgreSQL Database
```

---

# فناوری‌های استفاده‌شده

## Backend
- Python 3.11
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- Pydantic Settings
- JWT Authentication
- Passlib (bcrypt)
- HTTPX

## ai & machine learning
- Pandas
- NumPy
- Scikit-learn
- Prophet
- XGBoost
- TensorFlow
- NetworkX

## Frontend


- Next.js
- React
- TypeScript
- Tailwind CSS
- Axios
- TanStack Query
- Redux Toolkit
- React Redux
- Zustand
- Recharts
- Lucide React
- Classnames


## پایگاه داده

* PostgreSQL

---

# ساختار پروژه

```text
cclass_bi/
│
├── backend/
│   ├── app/
│   │   ├── ai_copilot/
│   │   ├── analytics/
│   │   ├── forecasting/
│   │   ├── dashboard/
│   │   ├── optimization/
│   │   ├── sales_opportunity/
│   │   ├── repositories/
│   │   ├── services/
│   │   └── api/
│   └── requirements.txt
│
├── cclass-dashboard/
│   ├── src/
│   ├── components/
│   ├── hooks/
│   ├── store/
│   └── package.json
│
├── README.md
└── .gitignore
```

---

# راه‌اندازی پروژه

## دریافت پروژه

```bash
git clone https://github.com/bt72-74/cclass.git

cd cclass
```

---

## اجرای Backend

```bash
cd backend

python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

آدرس سرویس:

```
http://localhost:8000
```

مستندات API:

```
http://localhost:8000/docs
```

---

## اجرای Frontend

```bash
cd cclass-dashboard

npm install

npm run dev
```

آدرس برنامه:

```
http://localhost:3000
```

---

# مستندات API

| سرویس       | آدرس                        |
| ----------- | --------------------------- |
| Backend API | http://localhost:8000       |
| Swagger UI  | http://localhost:8000/docs  |
| ReDoc       | http://localhost:8000/redoc |
| Frontend    | http://localhost:3000       |

---

# احراز هویت

این پروژه برای دسترسی به APIها از JWT Authentication استفاده می‌کند.

---

# برنامه‌های توسعه

* استقرار با Docker
* پشتیبانی از Kubernetes
* استفاده از Redis
* راه‌اندازی CI/CD
* مدیریت سطوح دسترسی کاربران
* معماری چندسازمانی (Multi-Tenant)
* توسعه قابلیت‌های هوش مصنوعی
* اعلان‌های بلادرنگ

---

# مشارکت در توسعه

در صورت تمایل می‌توانید پروژه را Fork کرده و پس از ایجاد تغییرات، Pull Request ارسال کنید.

---

# مجوز

این پروژه تحت مجوز MIT منتشر شده است.

---

# توسعه‌دهنده

BT72-74

https://github.com/bt72-74
