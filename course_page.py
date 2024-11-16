from selenium.webdriver.common.by import By
from base_page import BasePage

class CoursePage(BasePage):
    def add_course(self, course_name):
        self.enter_text(By.ID, "course-nome", course_name)
        self.click_element(By.ID, "course-btn")
        
    def get_course_result(self):
        return self.get_element_text(By.CSS_SELECTOR, ".py-p")
