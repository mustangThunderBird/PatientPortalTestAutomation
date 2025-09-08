from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import time

class PortalMessagingPage(BasePage):
    COMPOSE_MESSAGE_BTN = (By.CSS_SELECTOR, "button[title='Compose Message']")
    MESSAGE_IFRAME = (By.CSS_SELECTOR, "iframe[src*='messaging/messages.php']")
    LOADING_SPINNER = (By.CSS_SELECTOR, "div.alert.alert-info h3")
    SENT_COUNT = (By.XPATH, "//a[contains(.,'Sent')]/span")
    All_COUNT = ((By.XPATH, "//a[contains(.,'All')]/span"))
    ALL_TAB = (By.XPATH, "//a[contains(.,'All')]")
    ALL_MESSAGES_ROWS = (By.CSS_SELECTOR, "table tbody tr")
    TO_DROPDOWN = (By.ID, "selSendto")
    SUBJECT_INPUT = (By.ID, "title")
    BODY_EDITOR = (By.CSS_SELECTOR, "div.note-editable[contenteditable='true']")
    SEND_BTN = (By.ID, "submit")

    def get_all_count(self):
        count_elem = self.driver.find_element(*self.All_COUNT)
        return int(count_elem.text.strip())
    
    def get_sent_count(self):
        count_elem = self.driver.find_element(*self.SENT_COUNT)
        return int(count_elem.text.strip())
    
    def count_message_rows(self):
        rows = self.driver.find_elements(*self.ALL_MESSAGES_ROWS)
        # only count visible rows (skip ng-hide or template ones)
        visible_rows = [r for r in rows if r.is_displayed()]
        return len(visible_rows)
        
    def write_message_and_send(self, text):
        # Step 1: type into Summernote editor
        body = self.driver.find_element(*self.BODY_EDITOR)
        body.click()
        body.clear()
        body.send_keys(text)
        
        # Step 2: click Send
        self.driver.find_element(*self.SEND_BTN).click()
        
    def wait_for_message_page_to_load(self):
        # Step 1: wait and switch into iframe
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.MESSAGE_IFRAME))
        
        # Step 2: wait for loading spinner to disappear
        self.wait.until(EC.invisibility_of_element_located(self.LOADING_SPINNER))

    def send_message(self):
        # Step 1: wait for the compose button
        self.wait.until(EC.presence_of_element_located(self.COMPOSE_MESSAGE_BTN))
        button = self.driver.find_element(*self.COMPOSE_MESSAGE_BTN)
        button.click()
        time.sleep(1)
        
        # Step 2: select the person to send to
        dropdown = self.driver.find_element(*self.TO_DROPDOWN)
        send_to = Select(dropdown)
        send_to.select_by_index(0)
        time.sleep(0.5)
        
        # Step 3: Choose Pharmacy as subject
        subject_input = self.driver.find_element(*self.SUBJECT_INPUT)
        subject_input.clear()
        subject_input.send_keys("Pharmacy")
        time.sleep(0.5)
        
        # Step 4 Write and send message
        self.write_message_and_send("I need a refill of Zofran")
        time.sleep(3)
    
    def view_all_messages(self):
        self.click(self.ALL_TAB)
        time.sleep(.5)