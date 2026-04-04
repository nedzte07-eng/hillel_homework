from playwright.sync_api import Page, expect


class GaragePage:
    def __init__(self, page: Page):
        self._page = page
        self._alert_success = page.locator('//div[@class="alert alert-success"]')
        self._button_add_car = page.get_by_role("button", name="Add car")

    def get_alert_success(self):
        return self._alert_success

    def click_button_add_car(self):
        self._button_add_car.click()
        return True
