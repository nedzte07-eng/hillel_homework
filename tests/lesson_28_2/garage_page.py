from playwright.sync_api import Page, expect


class GaragePage:
    def __init__(self, page: Page):
        self._page = page
        self._alert_success = page.locator('//div[@class="alert alert-success"]')
        self._button_add_car = page.get_by_role("button", name="Add car")
        self._expenses_button = page.locator('//a[@routerlink="expenses"]')
        self._button_delete_car = page.locator('span.icon.icon-edit')
        self._header_name = page.get_by_role("heading", name="Garage")
        self._add_car_modal_title = page.locator("h4.modal-title")
        self._brand_selector = page.get_by_label("Brand")
        self._model_selector = page.get_by_label("Model")
        self._milleage_selector = page.get_by_role("spinbutton", name="Mileage")

    def get_alert_success(self):
        return self._alert_success

    def add_car(self):
        self._button_add_car.click()
        expect(self._add_car_modal_title).to_have_text("Add a car")
        self._brand_selector.select_option("3: 4")
        self._model_selector.select_option("6: 17")
        self._milleage_selector.click()
        self._milleage_selector.fill("880")
        self._page.get_by_role("button", name="Add").click()
        expect(self._page.locator("p:has-text('Car added')")).to_be_visible()
        return self._page

    def expenses_click(self):
        self._expenses_button.click()
        from tests.lesson_28_2.fuel_expences_page import FuelExpensesPage
        return FuelExpensesPage(self._page)

    def get_header_name(self):
        return self._header_name

    def delete_car(self):
        self._button_delete_car.click()
        self._page.get_by_role("button", name="Remove car").click()
        expect(self._page.get_by_role("heading", name="Remove car")).to_be_visible()
        self._page.get_by_role("button", name="Remove").click()
        expect(self._page.locator("p:has-text('Car removed')")).to_be_visible()
        return self._page
