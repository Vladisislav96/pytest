from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bases.base_class import Base

class Login_page(Base):
    url = "https://setivspb.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # локаторы
    menu_button="//a[@title='Мой кабинет']"
    user_name= "//*[@id='USER_LOGIN_POPUP']"
    password= "//*[@id='USER_PASSWORD_POPUP']"
    login_button= "//*[@id='avtorization-form']/div[3]/div[2]/input"

    #геттеры


    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.menu_button)))
    #actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name ")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("click login-button ")

    def click_menu_button(self):
        self.get_menu_button().click()
        print("click menu-button ")

    #методы

    def avtorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_menu_button()
        self.get_current_url()
        self.input_user_name("Vlados_9196@mail.ru")
        self.input_password("1234567")
        self.click_login_button()






