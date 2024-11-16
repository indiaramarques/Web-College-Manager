from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
    
    def wait_for_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        element = self.wait_for_element(by, value)
        element.click()

    def enter_text(self, by, value, text):
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by, value):
        element = self.wait_for_element(by, value)
        return element.text
