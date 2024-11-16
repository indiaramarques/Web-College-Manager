from selenium.webdriver.common.by import By
from base_page import BasePage

class DisciplinePage(BasePage):
    def add_discipline(self, discipline_name, course_id):
        self.enter_text(By.ID, "discipline-nome", discipline_name)
        self.enter_text(By.ID, "course-discipline-id", course_id)
        self.click_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn")
        
    def get_discipline_result(self):
        return self.get_element_text(By.CSS_SELECTOR, ".py-p")
