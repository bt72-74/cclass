# 🚀 C Class - Sales Analytics Dashboard

داشبورد تحلیل میزان فروش شرکت سی کلاس

## 📋 ساختار پروژه

```
cclass_bi/
├── backend/                    FastAPI Backend
│   ├── app/
│   ├── requirements.txt
│   └── ...
│
├── frontend/                   Next.js Frontend
│   ├── src/
│   ├── app/
│   ├── package.json
│   ├── tsconfig.json
│   └── ...
│
├── run-backend.bat            Windows Backend
├── run-frontend.bat           Windows Frontend
├── run-backend.ps1            PowerShell Backend
├── run-frontend.ps1           PowerShell Frontend
├── run-backend.sh             Linux/Mac Backend
├── run-frontend.sh            Linux/Mac Frontend
├── setup.bat                  Setup Script
├── cleanup.bat                Cleanup Script
├── .gitignore
└── README.md
```

## 🎯 شروع سریع

### ✅ اولین بار - Setup

```cmd
setup.bat
```

### ✅ Windows - Batch (ساده‌ترین)

**2 Command Prompt جداگانه:**

```cmd
REM Terminal 1
run-backend.bat

REM Terminal 2
run-frontend.bat
```

### ✅ Windows - PowerShell

```powershell
# Terminal 1
.\run-backend.ps1

# Terminal 2
.\run-frontend.ps1
```

### ✅ Linux / Mac

```bash
# Terminal 1
./run-backend.sh

# Terminal 2
./run-frontend.sh
```

### ✅ دستی

**Terminal 1:**
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

**Terminal 2:**
```bash
cd frontend
npm install
npm run dev
```

## 📍 آدرس‌ها

| سرویس | URL |
|-------|-----|
| 🎨 Frontend | http://localhost:3000 |
| 🔌 Backend API | http://localhost:8000 |
| 📚 API Swagger | http://localhost:8000/docs |
| 📖 ReDoc | http://localhost:8000/redoc |

## 🔐 ورود

```
نام کاربری: admin
رمز عبور: (تنظیم شده در backend)
```

## 📚 مستندات

- **Backend**: `backend/README.md`
- **Frontend**: `frontend/README.md` (اگر موجود)

## ⚙️ پیش‌نیازها

- Python 3.10+
- Node.js 18+
- npm یا yarn

## 💡 نکات

- Backend را **اول** شروع کنید
- از **دو Terminal جداگانه** استفاده کنید
- صبر کنید تا **dependencies نصب** شود

## 🧹 تمیز‌سازی

```cmd
cleanup.bat
```

---

**Happy Coding! 🎉**

