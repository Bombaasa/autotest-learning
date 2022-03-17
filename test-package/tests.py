import time
import random
from atf.ui import *
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.milestones_page import MilestonesPage


class TestNote(TestCaseUI):
    @classmethod
    # Выполняется 1 раз перед всеми тестами в классе
    def setup_class(cls):
        cls.browser.open('https://test-online.sbis.ru/')
        AuthPage(cls.driver).auth('Демо_тензор', 'Демо123')

    # Выполняется перед каждым тестом
    # def setup(self):

    # Сами тесты, обязательно префикс "test_"
    def test_01_create_check_and_remove_a_note(self):
        MainPage(self.driver).make_a_note()

    def test_02_milestone(self):
        milestone_test_name = 'Тестовая веха № ' + str(random.randint(1, 100000))
        milestone_test_description = 'Это веха для [ДАННЫЕ УДАЛЕНЫ]'
        time.sleep(1)  # Без этой задержки не успевает пройти авторизация
        self.browser.open('https://test-online.sbis.ru/page/milestones')
        MilestonesPage(self.driver).create_milestone(milestone_test_name, milestone_test_description)
        MilestonesPage(self.driver).check_milestone_exists(milestone_test_name, milestone_test_description)
        MilestonesPage(self.driver).open_opened_milestone_in_new_page()
        # self.browser.switch_to_new_window()
        MilestonesPage(self.driver).milestone_page_check(milestone_test_name, milestone_test_description)

    # Выполняется после каждого теста
    def teardown(self):
        self.browser.close_windows_and_alert()

    # Выполняется 1 раз после всех тестов в классе
    # @classmethod
    # def teardown_class(cls):


# Запуск тестов
if __name__ == '__main__':
    run_tests()
