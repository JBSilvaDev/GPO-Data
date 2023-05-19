
from controller.gpoController.gpo_controller import GpoController
from view.show_info_terminal import ShowInfoTerminal
from halo import Halo
from colorama import Fore, Style, Back


def main():
    # Cria uma instância do GpoController
    gpo_controller = GpoController()
    show_info_terminal = ShowInfoTerminal()

    while True:
        pec_numero = show_info_terminal.show_input("Digite o número da PEC (ou 'q' para sair):")
        print('*' * 100)
        
        if pec_numero.lower() == "q":
            spinner = Halo(text=" Encerrando programa...\n", spinner="dots")
            spinner.start()
            break

        spinner = Halo(text=" Aguardando retorno...", spinner="dots")
        spinner.start()

        text_info_pr_vao = gpo_controller.get_pr_vao(pec_numero)
        infos_pec = gpo_controller.get_info()

        spinner.stop()

        if text_info_pr_vao:
            dados_gpo = list(infos_pec)
            dados_gpo.append(text_info_pr_vao)
            show_info_terminal.show_gpo_item_list(dados_gpo, pec_numero)
        else:
            show_info_terminal.fail_find(f"{Back.WHITE}{Style.BRIGHT}{Fore.RED}Não foi possível obter as informações.{Style.RESET_ALL}{Fore.BLUE}{Style.RESET_ALL}")

    gpo_controller.kill_chrome()

    print("Programa encerrado!\nSe necessário feche este terminal.")
    spinner.stop()

if __name__ == "__main__":
    main()
