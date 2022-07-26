from selenium.webdriver.common.by import By


class MainPageLocators(object):

    SIGIN_BUTTON = (By.CSS_SELECTOR, '.desk-notif-card__login-new-item_enter.home-link_black_yes') #Кнопка логина на главной странице
    EMAIL_BUTTON = (By.XPATH, '//button[@data-type="login"]') #Кнопка входа по почте
    LOGIN_FIELD = (By.ID, 'passp-field-login') #Поле для ввода логина
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.Button2.Button2_view_action') #Кнопка Войти на форме ввода даных
    PASS_FIELD = (By.ID, 'passp-field-passwd') #Поле для ввода пароля
    DISK_LINK = (By.XPATH, "//a[@data-statlog='notifications.mail.login.disk']") #Ссылка на Я.Диск
    CREATE_BUTTON = (By.CSS_SELECTOR, '.create-resource-popup-with-anchor') #Кнопка создания на диске
    FOLDER_BUTTON = (By.CSS_SELECTOR, '.file-icon_dir_plus') #Кнопка выбора папки
    NAME_FIELD = (By.XPATH, '//form[@class="rename-dialog__rename-form"] // input') #Поле для ввода имени папки и файла
    CREATE_FOLDER_FILE_BUTTON = (By.CSS_SELECTOR, '.confirmation-dialog__button_submit') #Кнопка создания папки на форме
    FOLDER_ITEM = (By.XPATH, '//a[@href="/client/disk/SimbirUI"]') #Созданная папка на диске
    FILE_BUTTON = (By.CSS_SELECTOR, '.file-icon_doc') #Кнопка выбора файла
    ITEM_FILE = (By.CSS_SELECTOR, '.listing-item__fields') #Файл
    NAME_ITEM_FILE = (By.CSS_SELECTOR, '[aria-label="SimbirFile.docx"]') #Имя файла
    PROFILE_IMG = (By.CSS_SELECTOR, '.user-pic__image') #Иконка профиля
    LOGOUT_LINK = (By.CSS_SELECTOR, '.legouser__menu-item_action_exit') #Кнопка выхода из УЗ