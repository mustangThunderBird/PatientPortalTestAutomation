from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class PortalDocumentsPage(BasePage):
    UNAUTHORIZED_TEXT = (By.XPATH, "//*[contains(text(),'Unauthorized')]")

    def try_to_manually_switch_patient_id_in_url(self):
        # Step 1: grab current patient URL
        current_url = str(self.driver.current_url)
        pid = current_url.split("=")[1]

        # Step 2: craft a new URL with a different pid
        other_user_pid = int(pid) + 1
        target_url = f"{current_url.split('=')[0]}={other_user_pid}"

        # Step 3: navigate to the new URL
        self.driver.get(target_url)

        # Step 4: wait until the Unauthorized text appears
        try:
            elem = self.wait.until(EC.presence_of_element_located(self.UNAUTHORIZED_TEXT))
            return elem.text
        except:
            return None