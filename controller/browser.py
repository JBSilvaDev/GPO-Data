import subprocess
from subprocess import CREATE_NO_WINDOW
import platform
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
        # Executa o download do webdriver em um processo separado
        if platform.system() == "Windows":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.Popen(["python", "-m", "webdriver_manager.chrome", "--quiet"], startupinfo=startupinfo)
        else:
            subprocess.Popen(["python", "-m", "webdriver_manager.chrome", "--quiet"])

        # Aguarde um tempo para o download do webdriver ser concluído
        time.sleep(5)

        # Restante do seu código aqui
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-dev-shm-usage")
        prefsChrome = {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        }
        chrome_options.add_experimental_option("prefs", prefsChrome)

        service.creation_flags = CREATE_NO_WINDOW
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
