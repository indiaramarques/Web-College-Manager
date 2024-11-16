from selenium.webdriver.common.by import By
from base_page import BasePage

class HomePage(BasePage):
    def navigate_to_home(self):
        self.driver.get("https://tdd-detroid.onrender.com/")
        self.driver.set_window_size(970, 555)
        self.wait_for_element(By.ID, "py-internal-0")
