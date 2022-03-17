import time
from atf.ui import *


class MainPage(Region):
    saby_bird = Element(By.CSS_SELECTOR, '.icon-SabyBird', 'Открыть меню')
    menu_list = CustomList(By.CSS_SELECTOR, '.controls-Menu__content_singleLine', 'Пункты меню')
    editor_field = Element(By.CSS_SELECTOR, '.controls-RichEditor__editorFrame', 'Окно редактора заметки')
    ok_button = Element(By.NAME, 'okButton', 'ОК')
    notes_list = CustomList(By.NAME, 'noteContent', 'Все заметки')
    del_button = Element(By.CSS_SELECTOR, '[name=Remove]', 'Удалить')
    yes_button = Element(By.CSS_SELECTOR, '[name=positiveButton]', 'ДА')

    def make_a_note(self):
        """Создает, проверяет и удаляет заметку с текстом test_text"""

        test_text = 'Тестовая заметка. Она удалится через секунду.'
        self.saby_bird.click()
        self.menu_list.item(with_text='Заметка').click()
        self.editor_field.type_in(test_text)
        self.ok_button.click()
        self.notes_list.item(with_text=test_text).should_be(Visible, msg=
                                                        "Не появилась заметка", wait_time=True).click()
        self.del_button.click()
        time.sleep(1)  # Без этой задержки не удаляется. Видимо не успевает кнопка появляться
        self.yes_button.click()



