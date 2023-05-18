from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
from subprocess import CREATE_NO_WINDOW
from tqdm import tqdm
import os
os.environ["WDM_LOG_LEVEL"] = "0"
os.environ["WDM_HIDE_OUTPUT"] = "true"

tqdm.monitor_interval = 0





class BrowserController:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        service.creation_flags = CREATE_NO_WINDOW  # não exibir terminal chrome

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-dev-shm-usage")
        prefsChrome = {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        }
        chrome_options.add_experimental_option("prefs", prefsChrome)

        self.inBrowser = webdriver.Chrome(service=service, options=chrome_options)

    def wait_elements(self, element: str):
        maxLoop = 0
        listElement = self.inBrowser.find_elements(By.XPATH, element)
        while len(listElement) < 1 and maxLoop < 7:
            time.sleep(1)
            maxLoop += 1
        time.sleep(1)
        if len(listElement) < 1:
            print("Tempo esgotado, elemento não encontrado")
            return
        return self.inBrowser.find_element(By.XPATH, element)
