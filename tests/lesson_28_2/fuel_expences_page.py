from playwright.sync_api import Page, expect


class FuelExpensesPage:
    def __init__(self, page: Page):
        self._page = page
        self._header_name = page.get_by_role("heading", name="Fuel expenses")
        self._button_add_expenses = page.get_by_role("button", name="Add an expense")
        self._garage_button = page.locator('//a[@routerlink="garage"]')

    def get_header_name(self):
        return self._header_name

    def add_expenses(self):
        self._button_add_expenses.click()
        self._page.locator("#addExpenseMileage").click()
        self._page.locator("#addExpenseMileage").fill("890")
        self._page.get_by_label("Number of liters").fill('10')
        self._page.get_by_label("Total cost").fill('20')
        self._page.get_by_role("button", name="Add").click()
        expect(self._page.locator("p:has-text('Fuel expense added')")).to_be_visible()
        return self._page

    def garage_click(self):
        self._garage_button.click()
        from tests.lesson_28_2.garage_page import GaragePage
        return GaragePage(self._page)



