import time
from models.gpo_model import GpoModel
from controller.browser import BrowserController
from tqdm import tqdm
tqdm.monitor_interval = 0


class GpoController(BrowserController):
    def __init__(self):
        super().__init__()
        self.gpo_model = GpoModel()
        self.open_browser()

    def open_browser(self):
        self.inBrowser.get(self.gpo_model.links["home_login"])
        self.logon_gpo()

    def logon_gpo(self):
        self.wait_elements(
            "/html/body/form/center/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td[2]/input"
        ).send_keys(self.gpo_model.usuario)
        self.wait_elements(
            "/html/body/form/center/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/input"
        ).send_keys(self.gpo_model.senha)
        self.wait_elements('//*[@id="tbrImg"]').click()

    def getPrVao(self, pec:str, textInfoPrVao):
        self.inBrowser.get(self.gpo_model.links["prvao"] + pec)
        try:
            pr_element = self.wait_elements('//*[@id="TQuery"]/tbody/tr[2]/td[2]')
            pr = pr_element.text.strip() if pr_element else 'Não liberada'
            
            vao_element = self.wait_elements('//*[@id="TQuery"]/tbody/tr[2]/td[3]')
            vao = vao_element.text[:4].strip() if vao_element else 'AV'
        except:
            pr = 'Não liberada'
            vao = 'AV'
        textInfoPrVao.set(f"PR {pr} - VÃO {vao}")

    def killChrome(self):
        self.inBrowser.close()
