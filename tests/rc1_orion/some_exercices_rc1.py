import os
import asyncio
from playwright.async_api import async_playwright
from dotenv import load_dotenv

# Завантажуємо змінні середовища
load_dotenv()

BASE_URL = os.getenv("RC1_ORION")
if not BASE_URL:
    raise ValueError("❌ RC1_ORION не знайдено у .env")

USER_EMAIL = os.getenv("RC1_ORION_EMAIL")
USER_PASSWORD = os.getenv("RC1_ORION_PASSWORD")
BASIC_AUTH_USER = os.getenv("RC1_ORION_BASIC_USER")
BASIC_AUTH_PASS = os.getenv("RC1_ORION_BASIC_PASS")


async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # headless=False щоб бачити процес

        # Додаємо базову авторизацію
        context = await browser.new_context(
            http_credentials={
                "username": BASIC_AUTH_USER,
                "password": BASIC_AUTH_PASS}
        )
        page = await context.new_page()

        # 1. Перехід на сторінку логіну
        await page.goto(f"{BASE_URL}/login")

        # 2. Введення логіну/паролю
        await page.fill('input[name="email"]', USER_EMAIL)
        await page.fill('input[name="password"]', USER_PASSWORD)
        await page.click('button[type="submit"]')

        # 3. Очікуємо редірект після логіну
        await page.wait_for_url(BASE_URL)

        # 4. Витягуємо токен із cookies
        cookies = await context.cookies()
        session_cookie = next((c for c in cookies if c["name"] == "orion_rc_1_session"), None)
        if session_cookie:
            print(f"Session token: {session_cookie["value"]}" )
        else:
            print("⚠️ Cookie 'orion_rc_1_session' не знайдено")

        await browser.close()

asyncio.run(run())

