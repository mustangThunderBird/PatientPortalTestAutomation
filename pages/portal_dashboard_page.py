from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class PortalDashboardPage(BasePage):
    LOGOUT_URL = r"https://demo.openemr.io/openemr./logout.php"
    LOGOUT_BTN = (By.LINK_TEXT, "Logout")
    PROFILE_BTN = (By.ID, "profile-go")
    APPOINTMENTS_BTN = (By.ID, "appointments-go")
    DASHBOARD_BTN = (By.ID, "quickstart_dashboard")
    MESSAGING_BTN = (By.ID, "messages-go")
    DOCUMENTS_BTN = (By.ID, "documents-go")

    def is_logged_in(self):
        return self.is_visible(self.DASHBOARD_BTN)

    def logout(self):
        self.click(self.LOGOUT_BTN)
        
    def is_logged_out(self):
        return EC.url_matches(self.LOGOUT_URL)
    
    def go_to(self, tab:str):
        if tab.lower() == "profile":
            self.click(self.PROFILE_BTN)
        elif tab.lower() == "appointments":
            self.click(self.APPOINTMENTS_BTN)
        elif tab.lower() == "messaging":
            self.click(self.MESSAGING_BTN)
        elif tab.lower() == "documents":
            self.click(self.DOCUMENTS_BTN)
        else:
            if not isinstance(tab, str):
                raise AttributeError(f"Error... recieved type {type(tab)} for tab when it should be str...")
            else:
                raise ValueError(f"Error... invalid str argument for tab...")
