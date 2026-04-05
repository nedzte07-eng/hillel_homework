from playwright.sync_api import Page, expect


class GaragePage:
    def __init__(self, page: Page):
        self._page = page
        self._alert_success = page.locator('//div[@class="alert alert-success"]')
        self._button_add_car = page.get_by_role("button", name="Add car")
        self._expenses_button = page.locator('//a[@routerlink="expenses"]')

    def get_alert_success(self):
        return self._alert_success


    def add_car(self):
        self._button_add_car.click()
        expect(self._page.locator("h4.modal-title")).to_have_text("Add a car")
        self._page.get_by_label("Brand").select_option("3: 4")
        self._page.get_by_label("Model").select_option("6: 17")
        # assert page.get_by_label("Model").inner_text() == "Cayenne"
        self._page.get_by_role("spinbutton", name="Mileage").click()
        self._page.get_by_role("spinbutton", name="Mileage").fill("880")
        self._page.get_by_role("button", name="Add").click()
        expect(self._page.locator("p:has-text('Car added')")).to_be_visible()
        return self._page

    def expenses_click(self):
        self._expenses_button.click()
        from tests.lesson_28_2.fuel_expences_page import FuelExpencesPage
        return FuelExpencesPage(self._page)


