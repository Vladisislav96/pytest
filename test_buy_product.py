import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from page.catalog import Catalog
from page.kart_page import Kart_page
from page.login_page import Login_page
from page.select_dva import Select_dva


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start Test")


    login = Login_page(driver)
    login.avtorization()
    sl=Select_dva(driver)
    sl.sl()



    kp=Kart_page(driver)
    kp.product_confirmation()


    #методы



