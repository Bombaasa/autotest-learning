import time

from atf.ui import *
from pages_inside.edo_controls.edo3dialog import Edo3Dialog
from pages_inside.edo_controls.saby_page import MasterDetail


class MilestonesPage(Edo3Dialog, MasterDetail):
    name = ControlsInputText(By.CSS_SELECTOR, '.ms-SecondLineContent__name', 'Название')
    description = ControlsInputArea(By.CSS_SELECTOR, '.ms-SecondLineContent__descriptionContainer', 'Описание')
    # addButton = ControlsButton(By.CSS_SELECTOR, '.icon-RoundPlus', 'Добавить')
    addButton = MasterDetail.add_button
    menu = ControlsMenuControl(By.CSS_SELECTOR, '.controls-menu', '[title="Веха ТОП"]')
    searchField = ControlsSearchInput()

    def create_milestone(self, milestone_name, milestone_description):
        """Создает веху с регламентом Веха ТОП, с названием milestone_name и
         описанием milestone_description"""

        time.sleep(1)  # Без задержки не успевает кнопка нажаться
        self.addButton.click()
        self.menu.click()
        self.check_open()
        self.name.type_in(milestone_name)
        self.description.type_in(milestone_description)
        self.save()
        self.check_close()

    def check_milestone_exists(self, milestone_name, milestone_description):
        """Проверяет что веха с названием milestone_name и
         описанием milestone_description существует в регистре"""

        self.search(milestone_name, search_btn_click=True)
        self.search_and_open(milestone_name)
        self.check_open()
        self.name.should_be(ContainsText(milestone_name))
        self.description.should_be(ContainsText(milestone_description))

    def open_opened_milestone_in_new_page(self):
        """Открывает открытую веху в новой вкладке"""

        self.select_service_command('Ссылка', 'Открыть в новой вкладке')

    def milestone_page_check(self, milestone_name, milestone_description):
        """Проверяет веху на её личной странице (после открытия в новом окне
        или при переходе по ссылке)"""

        self.check_open()
        self.name.should_be(ContainsText(milestone_name))
        self.description.should_be(ContainsText(milestone_description))
