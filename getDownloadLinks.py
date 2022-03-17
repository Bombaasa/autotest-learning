import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestDownloadlinks():
    def setup_method(self, method):
        self.driver = webdriver.Chrome(executable_path='/home/local/TENSOR-CORP/aa.krotov/PycharmProjects/testing/chromedriver')
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_downloadlinks(self):
        self.driver.get("https://sbis.ru/")
        self.driver.set_window_size(1263, 1080)
        self.driver.find_element(By.LINK_TEXT, "Поддержка").click()
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located
                                           ((By.XPATH,
                                            '//*[@id="container"]/div[2]/div/div[3]/div/div/div[2]/div/div[3]/a')))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[3]/div/div/div[2]/div/div[3]/a').click()
        time.sleep(2)
        links = self.driver.find_elements_by_class_name('sbis_ru-DownloadNew-loadLink__link')
        with open('output.txt', 'w') as f:
            for i in links:
                if i.is_displayed():
                    f.write(i.get_attribute('href'))
                    f.write("\n")
