import os

from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv(dotenv_path=r"C:\Users\nedzt\Documents\Study\QA Automation Python\hillel_homework\.env")


class LoginPage:
    def __init__(self, page: Page):
        """Конструктор отримує об'єкт page та зберігає його"""
        self.page = page
        # Локатори елементів сторінки (приватні)
        self._button_sign_in = page.locator('//button[@class="btn btn-outline-white header_signin"]')
        self._email_input = page.get_by_role("textbox", name="Email")
        self._password_input = page.get_by_role("textbox", name="Password")
        self._submit_button = page.get_by_role("button", name="Login")
        self._ui_url = os.getenv('API_URL')

    def navigate(self):
        """Метод для переходу на сторінку"""
        self.page.goto(self._ui_url)
        return self

    def enter_email(self, email: str):
        self._email_input.fill(email)
        return self

    def enter_password(self, password: str):
        self._password_input.fill(password)
        return self

    def submit_button(self):
        self._submit_button.click()
        from garage_page import GaragePage
        return GaragePage(self.page)

    def submit(self, email: str, password: str):
        """Комбінований метод для входу (ланцюжок)"""
        self.enter_email(email)
        self.enter_password(password)
        return self.submit_button()
