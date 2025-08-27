import os
import datetime

def screenshot_on_failure(driver, test_name):
    """
    Saves a screenshot into reports/ folder with timestamp and test name.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs("reports", exist_ok=True)
    file_path = os.path.join("reports", f"{test_name}_{timestamp}.png")
    driver.save_screenshot(file_path)
    print(f"[!] Screenshot saved to {file_path}")