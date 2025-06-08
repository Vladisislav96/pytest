import sys
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.core import driver

from bases.base_class import Base


class   Select_dva(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #локаторы
    Top_2024="//*[@id='content']/div/div[2]/div[1]/ul/li[12]"
    sovet="//*[@id='content']/div[2]/div[2]/div[2]/div/form/div[2]/div[3]/div[2]/div[1]/label[2]/span/span"
    min_price="//*[@id='NEXT_SMART_FILTER_P1_MIN']"
    max_price="//input[@class='max-price']"
    brend="//*[@id='content']/div[2]/div[2]/div[2]/div/form/div[2]/div[4]/div[2]/div[1]/label[1]/span"
    open="//*[@id='set_filter']"
    select_pr="//*[@id='bx_3966226736_12021']/div/div[2]/div[1]/a/span"
    enter_cart="//span[@data-value='4987.5']"
    gou_in_cart = "//*[@id='bx_basketT0kNhm']/div/a"
    main_word = "//*[@id='pagetitle']"

    def get_Top_2024(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Top_2024)))
    def get_sovet(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sovet)))
    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))
    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))
    def get_brend(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brend)))
    def get_open(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.open)))
    def get_select_pr(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_pr)))

    def get_enter_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_cart)))
    def get_gou_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gou_in_cart)))
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    #action

    def click_Top_2024(self):
        self.get_Top_2024().click()
        print("зашел в топ 2024")
    def click_sovet(self):
        self.get_sovet().click()
        print("выбрал совет")
    def send_min_price(self):
        self.get_min_price().send_keys("4000")
        print("ввел минимальное значение")
    def send_max_price(self):
        self.get_max_price().send_keys("7000")
        print("ввел максимальное значение")
    def click_brend(self):
        self.get_brend().click()
        print("выбрал бренд")
    def click_open(self):
        self.get_open().click()
        print("открыл отфильтрованные товары")
    def click_select_pr(self):
        self.get_select_pr().click()
        print("выбрал товар ")
    def click_enter_cart(self):
        self.get_enter_cart().click()
        print("кликнул по товару  и добавил в корзину ")
    def click_gou_in_cart(self):
        self.get_gou_in_cart().click()
        print("перешел в корзину")





    #metody
    def sl(self):
        self.get_current_url()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)
        self.click_Top_2024()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 400)")
        self.send_min_price()
        time.sleep(2)
        self.send_max_price()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 700)")
        self.click_sovet()
        time.sleep(2)

        self.click_brend()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 700)")
        self.click_open()
        self.click_select_pr()
        self.click_enter_cart()
        #self.assert_word(self.get_main_word(),"Корзина")
        #print("мы действительно находимся в корзине")
        print("дальше отрабатывает класс kart_page")




