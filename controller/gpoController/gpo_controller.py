import time

from models.gpo_model import GpoModel
from controller.browser import BrowserController


class GpoController(BrowserController):
    def __init__(self):
        super().__init__()
        self.gpo_model = GpoModel()
        self.open_browser()

    def open_browser(self):
        self.in_browser.get(self.gpo_model.links["home_login"])
        self.login_gpo()

    def login_gpo(self):
        self.wait_elements(
            "/html/body/form/center/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td[2]/input"
        ).send_keys(self.gpo_model.usuario)
        self.wait_elements(
            "/html/body/form/center/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/input"
        ).send_keys(self.gpo_model.senha)
        self.wait_elements('//*[@id="tbrImg"]').click()

    def get_pr_vao(self, pec):
        self.in_browser.get(self.gpo_model.links["prvao"] + pec)
        try:
            pr_element = self.wait_elements('//*[@id="TQuery"]/tbody/tr[2]/td[2]')

            pr = pr_element.text.strip() if pr_element else "Não liberada"

            vao_element = self.wait_elements('//*[@id="TQuery"]/tbody/tr[2]/td[3]')
            vao = vao_element.text[:4].strip() if vao_element  else "AV"

        except:
            pr = "Não liberada"
            vao = "AV"
        return f"PR {pr} - VÃO {vao}"

    def get_info(self):
        try:
            marcacao = self.wait_elements(
                '//*[@id="frmPrincipal"]/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input[3]'
            )

            marcacao = (
                marcacao.get_attribute("value").strip()
                if marcacao
                else "Não disponivel"
            )

            ubc = self.wait_elements(
                '//*[@id="frmPrincipal"]/table/tbody/tr[2]/td/table/tbody/tr[10]/td[2]/input'
            )
            ubc = ubc.get_attribute("value").strip() if ubc else "Não disponivel"

            material = self.wait_elements(
                '//*[@id="frmPrincipal"]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/input[3]'
            )
            material = (
                material.get_attribute("value").strip()
                if material
                else "Não disponivel"
            )

            agendado = self.wait_elements('//*[@id="TQuery"]/tbody/tr[2]/td[5]')
            agendado = agendado.text.strip() if agendado else "0"
            recebido = self.wait_elements('//*[@id="TQuery"]/tbody/tr[2]/td[6]')
            recebido = recebido.text.strip() if recebido else "0"
            restante = f"{int(agendado) - int(recebido)}"
        except:
            marcacao = "Não Disponivel"
            agendado = "0"
            recebido = "0"
            restante = "0"
            material = "Não Disponivel"
            ubc = "Não Disponivel"
        return marcacao, agendado, recebido, restante, material, ubc

    def kill_chrome(self):
        self.in_browser.close()
        self.in_browser.service.stop()

