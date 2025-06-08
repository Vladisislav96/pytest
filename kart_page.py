import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.core import driver

from bases.base_class import Base


class   Kart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #локаторы
    checkout_button="//*[@id='bx_basketT0kNhm']/div/a"
    oformlenie="//*[@id='pagetitle']"




    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))
    def get_oformlenie(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.oformlenie)))

    #action

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("перешел в оформление заказа")




    #metody
    def product_confirmation(self):
        self.get_current_url()
        time.sleep(2)
        self.click_checkout_button()
        self.assert_word(self.get_oformlenie(), "Корзина")
        print("находимся в корзине")
        print("finish")



