from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class PortalProfilePage(BasePage):
    PROFILE_CARD = (By.ID, "profilecard")
    NAME_FIELD = (By.XPATH, "//td[contains(text(), 'Name')]/following-sibling::td")
    DOB_FIELD = (By.XPATH, "//td[contains(text(), 'DOB')]/following-sibling::td")
    PHONE_FIELD = (By.XPATH, "//td[contains(text(), 'Home Phone')]/following-sibling::td")
    ADDRESS_FIELD = (By.XPATH, "//td[contains(text(), 'Address')]/following-sibling::td")

    def is_profile_visible(self):
        """Check that profile card div has 'show' class (expanded)."""
        card = self.driver.find_element(*self.PROFILE_CARD)
        return "show" in card.get_attribute("class")

    def get_field_text(self, locator):
        """Return trimmed text for a given field locator."""
        return self.driver.find_element(*locator).text.strip()

    def demographics_present(self):
        """Verify key fields are visible and non-empty."""
        return all([
            self.get_field_text(self.NAME_FIELD) != "",
            self.get_field_text(self.DOB_FIELD) != "",
            self.get_field_text(self.PHONE_FIELD) != "",
            self.get_field_text(self.ADDRESS_FIELD) != "",
        ])
        
    def is_dob_formatted(self):
        """Verify that DOB_FIELD is formatted as YYYY-MM-DD"""
        dob = self.get_field_text(self.DOB_FIELD)
        year, month, day = map(int, dob.split("-"))
        return (1900 <= year <= 2100) and (1 <= month <= 12) and (1 <= day <= 31)
    
    def is_phone_formatted(self):
        """Verify that PHONE_FIELD is formatted as ###-###-####"""
        phone = self.get_field_text(self.PHONE_FIELD)
        ac,first3,last4 = map(int, phone.split("-"))
        return isinstance(ac, int) and isinstance(first3, int) and isinstance(last4, int)
    