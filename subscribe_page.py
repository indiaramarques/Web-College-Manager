from selenium.webdriver.common.by import By
from base_page import BasePage

class SubscribePage(BasePage):
    def subscribe_student_to_course(self, student_id, course_id):
        self.enter_text(By.ID, "student-id", student_id)
        self.enter_text(By.ID, "course-id", course_id)
        self.click_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #course-btn")
    
    def subscribe_student_to_discipline(self, student_id, discipline_id):
        self.enter_text(By.ID, "subscribe-student-id", student_id)
        self.enter_text(By.ID, "subscribe-discipline-id", discipline_id)
        self.click_element(By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn")

    def get_subscription_result(self):
        return self.get_element_text(By.CSS_SELECTOR, ".py-p")
