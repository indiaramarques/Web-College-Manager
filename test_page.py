import pytest
import time
from selenium import webdriver
from home_page import HomePage
from student_page import StudentPage
from course_page import CoursePage
from discipline_page import DisciplinePage
from subscribe_page import SubscribePage

class TestDemo:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)
        self.student_page = StudentPage(self.driver)
        self.course_page = CoursePage(self.driver)
        self.discipline_page = DisciplinePage(self.driver)
        self.subscribe_page = SubscribePage(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        self.home_page.navigate_to_home()

        # Adiciona aluno
        self.student_page.add_student("douglas")
        result_string = self.student_page.get_student_result()
        expected_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        assert result_string.startswith(expected_time)
        assert result_string.endswith("INFO Added student id: 1, Name: douglas")

        # Adiciona curso
        self.course_page.add_course("mat")
        result_string = self.course_page.get_course_result()
        assert result_string.startswith(expected_time)
        assert result_string.endswith("INFO Added course id: 1, Nome: mat")

        # inscrição do aluno em curso
        self.subscribe_page.subscribe_student_to_course("1", "1")
        result_string = self.subscribe_page.get_subscription_result()
        assert result_string.startswith(expected_time)
        assert result_string.endswith("INFO Student id 1 subscribed to course id 1")

        # Adiciona disciplina com falha (não há cursos suficientes)
        self.discipline_page.add_discipline("mat", "1")
        result_string = self.discipline_page.get_discipline_result()
        assert result_string.startswith(expected_time)
        assert result_string.endswith("FAIL Necessários 3 cursos para se criar a primeira matéria")

        # Adiciona mais cursos
        self.course_page.add_course("port")
        result_string = self.course_page.get_course_result()
        expected_time_port = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        assert result_string.startswith(expected_time_port)
        assert result_string.endswith("INFO Added course id: 2, Nome: port")

        self.course_page.add_course("geo")
        result_string = self.course_page.get_course_result()
        expected_time_geo = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        assert result_string.startswith(expected_time_geo)
        assert result_string.endswith("INFO Added course id: 3, Nome: geo")
        
        # Adiciona disciplinas e se inscreve
        
        self.discipline_page.add_discipline("mat", "1")
        self.discipline_page.add_discipline("mat2", 1)
        self.discipline_page.add_discipline("mat3", 1)

        self.subscribe_page.subscribe_student_to_discipline(1, 1) 
        self.subscribe_page.subscribe_student_to_discipline(1, 2)
        self.subscribe_page.subscribe_student_to_discipline(1, 3)
        result_string = self.subscribe_page.get_subscription_result()
        
        expected_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        assert result_string.startswith(expected_time)
        assert result_string.endswith("Name douglas subscribed to discipline id 3")

        time.sleep(3)
        