from selenium.webdriver.common.by import By
from base_page import BasePage

class StudentPage(BasePage):
    def add_student(self, student_name):
        self.enter_text(By.ID, "student-nome", student_name)
        self.click_element(By.ID, "student-btn")
        
    def get_student_result(self):
        return self.get_element_text(By.CSS_SELECTOR, ".py-p")
