from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from utils import locators
import time


class MainPage(BasePage):

    def __init__(self, driver):
        self.locator = locators.MainPageLocators
        super().__init__(driver)

    def login_yandex(self):
        """ Нажимает на кнопку входа """
        self.find_element(*self.locator.SIGIN_BUTTON).click()

    def enter_login(self):
        """ Вводим логин """
        self.find_element(*self.locator.EMAIL_BUTTON).click()
        time.sleep(2)
        login_field = self.find_element(*self.locator.LOGIN_FIELD)
        time.sleep(1)
        login_field.send_keys('TZApiSimbir')
        self.find_element(*self.locator.LOGIN_BUTTON).click()
        time.sleep(1)

    def enter_password(self):
        """ Вводим пароль """
        password_field = self.find_element(*self.locator.PASS_FIELD)
        time.sleep(2)
        password_field.send_keys('SimbirS0ft')
        self.find_element(*self.locator.LOGIN_BUTTON).click()
        time.sleep(2)

    def go_disk(self):
        """ Переходим на Я.Диск """
        self.find_element(*self.locator.DISK_LINK).click()
        disk_window = self.driver.window_handles[1]
        self.driver.switch_to.window(disk_window)
        time.sleep(2)

    def create_folder(self):
        """ Создаём папку """
        self.find_element(*self.locator.CREATE_BUTTON).click()
        time.sleep(1)
        self.find_element(*self.locator.FOLDER_BUTTON).click()
        time.sleep(1)
        name_field = self.find_element(*self.locator.NAME_FIELD)
        name_field.click()
        name_field.send_keys(Keys.CONTROL + "a")
        name_field.send_keys(Keys.DELETE)
        self.find_element(*self.locator.NAME_FIELD).send_keys('SimbirUI')
        self.find_element(*self.locator.CREATE_FOLDER_FILE_BUTTON).click()
        time.sleep(2)

    def go_folder(self):
        """ Переходим в папку """
        self.find_element(*self.locator.FOLDER_ITEM).click()

    def create_file(self):
        """ Создаём файл """
        self.find_element(*self.locator.CREATE_BUTTON).click()
        time.sleep(1)
        self.find_element(*self.locator.FILE_BUTTON).click()
        time.sleep(1)
        name_field = self.find_element(*self.locator.NAME_FIELD)
        name_field.click()
        name_field.send_keys(Keys.CONTROL + "a")
        name_field.send_keys(Keys.DELETE)
        self.find_element(*self.locator.NAME_FIELD).send_keys('SimbirFile')
        self.find_element(*self.locator.CREATE_FOLDER_FILE_BUTTON).click()

    def close_file(self):
        """ Закрываем файл """
        disk_window = self.driver.window_handles[1]
        self.driver.switch_to.window(disk_window)
        time.sleep(2)


    def should_be_new_file(self):
        """ Проверяем создан ли файл """
        assert self.is_element_present(*self.locator.NAME_ITEM_FILE), "File is presented"

    def logout(self):
        """ Выходим из аккаунта """
        self.find_element(*self.locator.PROFILE_IMG).click()
        self.find_element(*self.locator.LOGOUT_LINK).click()