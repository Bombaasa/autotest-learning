from atf.ui import *


class AuthPage(Region):
    login = Element('css selector', '[name=Login]', 'Логин')
    password = Element(By.CSS_SELECTOR, '[name=Password]', 'Пароль')
    enter_btn = Element(By.CSS_SELECTOR, '.icon-TFFollow', 'Войти')

    def auth(self, user_login, user_password):
        """Авторизуется на странице авторизации под
        логином user_login и паролем user_password"""

        self.login.type_in(user_login)
        self.enter_btn.click()
        self.password.type_in(user_password)
        self.enter_btn.click()
