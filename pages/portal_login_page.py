from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class PortalLoginPage(BasePage):
    USERNAME = (By.ID, "uname")
    PASSWORD = (By.ID, "pass")
    EMAIL = (By.ID, "passaddon")
    LOGIN_BTN = (By.CSS_SELECTOR, 'button.btn-success')
    
    def login(self, username, password, email):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.type(self.EMAIL, email)
        self.click(self.LOGIN_BTN)