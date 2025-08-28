from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class PortalDashboardPage(BasePage):
    LOGOUT_URL = r"https://demo.openemr.io/openemr./logout.php"
    LOGOUT_BTN = (By.LINK_TEXT, "Logout")
    PROFILE_BTN = (By.XPATH, '//*[@id="profile-go"]/div/button')
    DASHBOARD_BTN = (By.ID, "quickstart_dashboard")

    def is_logged_in(self):
        return self.is_visible(self.DASHBOARD_BTN)

    def logout(self):
        self.click(self.LOGOUT_BTN)
        
    def is_logged_out(self):
        return EC.url_matches(self.LOGOUT_URL)
    
    def go_to(self, tab:str):
        if tab.lower() == "profile":
            self.click(self.PROFILE_BTN)
        else:
            if not isinstance(tab, str):
                raise AttributeError(f"Error... recieved type {type(tab)} for tab when it should be str...")
            else:
                raise ValueError(f"Error... invalid str argument for tab...")
