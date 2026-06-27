import json
import httpx
from app.core.config import settings

MODEL = "gemini-2.0-flash"

SYSTEM_PROMPT = """تو یک دستیار هوشمند تجاری هستی که به مدیران و فروشندگان یک شرکت لوازم‌التحریر کمک می‌کنی.

وقتی داده‌های کسب‌وکار بهت داده میشه، اونا رو تحلیل کن و پاسخ دقیق، مفید و خلاصه بده.
اگر داده‌ای نداری، بر اساس دانش عمومی‌ات راهنمایی کن.
همیشه به فارسی پاسخ بده. پاسخ‌ها رو خوانا، کوتاه و کاربردی نگه‌دار.
از emoji برای خوانایی بیشتر استفاده کن."""


def llm_analyze(prompt: str, business_data: dict = None) -> str:
    api_key = settings.GEMINI_API_KEY.strip()

    if not api_key:
        return "⚙️ GEMINI_API_KEY در فایل .env تنظیم نشده."

    if business_data:
        data_str = json.dumps(business_data, ensure_ascii=False, indent=2)
        user_content = f"داده‌های کسب‌وکار:\n```json\n{data_str}\n```\n\nسوال کاربر: {prompt}"
    else:
        user_content = prompt

    try:
        response = httpx.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={api_key}",
            headers={"Content-Type": "application/json"},
            json={
                "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
                "contents": [{"parts": [{"text": user_content}]}],
                "generationConfig": {"maxOutputTokens": 1024},
            },
            timeout=20,
        )

        if response.status_code == 200:
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]

        return f"⚠️ خطای API: {response.status_code} — {response.text[:300]}"

    except httpx.TimeoutException:
        return "⏱️ زمان انتظار تموم شد. لطفاً دوباره امتحان کنید."
    except httpx.ConnectError:
        return "🔌 اتصال به سرور AI برقرار نشد."
    except Exception as e:
        return f"❌ خطا: {str(e)}"
