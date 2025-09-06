from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time
from datetime import datetime


class PortalAppointmentsPage(BasePage):
    APPOINTMENTS_CARD = (By.ID, "appointmentcard")
    SCHEDULE_APPOINTMENT_BTN = (By.LINK_TEXT, "Schedule A New Appointment")
    SEE_AVAILABILITY_BTN = (By.CSS_SELECTOR, "input.btn.btn-success[value='See Availability']")
    IFRAME = (By.ID, "modalframe") 
    APPOINTMENT_LINKS = (By.CSS_SELECTOR, "td.srTimes a")
    SAVE_APPOINTMENT_BUTTON = (By.NAME, "form_save")
    APPOINTMENT_CARDS = (By.CSS_SELECTOR, "#appointmentcard .card-body.font-weight-bold p")
                
    def request_appointment(self):
        appointment_saved = False
                
        self.click(self.SCHEDULE_APPOINTMENT_BTN)
        time.sleep(0.5)

        # Step 1: click See Availability
        btn = self.wait.until(EC.element_to_be_clickable(self.SEE_AVAILABILITY_BTN))
        self.driver.execute_script("arguments[0].click();", btn)
        
        # Step 2: switch into the iframe
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.IFRAME))

        # Step 3: wait for table to appear
        links = self.wait.until(EC.presence_of_all_elements_located(self.APPOINTMENT_LINKS))
        if not links:
            raise Exception("No appointment slots found")

        # Step 4: select the last available time slot
        time.sleep(0.5)
        chosen = links[-1]
        
        # Click the slot
        self.driver.execute_script("arguments[0].scrollIntoView(true);", chosen)
        chosen.click()
        time.sleep(1)
        
        #Step 5 switch back to main DOM
        self.driver.switch_to.default_content()
        
        #Step 6 save appointment
        self.click(self.SAVE_APPOINTMENT_BUTTON)
        appointment_saved = True
            
        return appointment_saved