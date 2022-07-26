from tests.base_test import BaseTest
from pages.main_page import *


class TestYandexDisk(BaseTest):
    def test_disk1(self):
        page = MainPage(self.driver)  # Переходим на яндекс
        page.login_yandex()  # Нажимаем вход
        page.enter_login()
        page.enter_password()
        page.go_disk()
        page.create_folder()
        page.go_folder()
        page.create_file()
        page.close_file()
        page.should_be_new_file()
        page.logout()