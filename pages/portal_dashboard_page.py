from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PortalDashboardPage(BasePage):
    LOGOUT_BTN = (By.LINK_TEXT, "Logout")
    DASHBOARD_BTN = (By.ID, "quickstart_dashboard")

    def is_logged_in(self):
        return self.is_visible(self.DASHBOARD_BTN)

    def logout(self):
        self.click(self.LOGOUT_BTN)
