from playwright.sync_api import Page, expect


class FuelExpencesPage:
    def __init__(self, page: Page):
        self._page = page
        self._header_name = page.get_by_role("heading", name="Fuel expenses")

    def get_header_name(self):
        return self._header_name


