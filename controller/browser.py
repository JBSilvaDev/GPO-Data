from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time


class BrowserController:
    def __init__(self):
        service = Service(ChromeDriverManager().install())

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--log-level=3")

        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-dev-shm-usage")
        prefs_chrome = {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        }
        chrome_options.add_experimental_option("prefs", prefs_chrome)

        self.in_browser = webdriver.Chrome(service=service, options=chrome_options)

    def wait_elements(self, element):
        max_loop = 0
        list_elements = self.in_browser.find_elements(By.XPATH, element)
        while len(list_elements) < 1 and max_loop < 10:
            time.sleep(1)
            max_loop += 1
        time.sleep(1)
        if len(list_elements) < 1:
            print("Tempo esgotado, elemento não encontrado")
            return
        return self.in_browser.find_element(By.XPATH, element)
