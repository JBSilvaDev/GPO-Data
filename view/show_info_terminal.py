from colorama import Fore, Style, Back


class ShowInfoTerminal:
    def __init__(self):
        pass

    def show_gpo_item_list(self, msg, pec_num):
        header = f"PR - {pec_num} | UBC - {msg[5]}"
        material = f"Material: {msg[4]}"
        output = f"""
{'=' * 100}
{Back.BLACK}{Style.BRIGHT}{Fore.WHITE}{header.center(100)}{Style.RESET_ALL}
{Back.BLACK}{material.center(100)}{Style.RESET_ALL}
{'=' * 100}
{Fore.GREEN}Pr/Vão -> {Style.RESET_ALL}{Fore.BLUE}{msg[-1]}{Style.RESET_ALL}
{Fore.RED}{'-' * 100}{Style.RESET_ALL}
{Fore.GREEN}Marcação -> {Style.RESET_ALL}{Fore.BLUE}{msg[0]}{Style.RESET_ALL}
{Fore.RED}{'-' * 100}{Style.RESET_ALL}
{Fore.GREEN}Agendado -> {Style.RESET_ALL}{Fore.BLUE}{msg[1]}{Style.RESET_ALL}
{Fore.RED}{'-' * 100}{Style.RESET_ALL}
{Fore.GREEN}Recebido Porto -> {Style.RESET_ALL}{Fore.BLUE}{msg[2]}{Style.RESET_ALL}
{Fore.RED}{'-' * 100}{Style.RESET_ALL}
{Fore.GREEN}Entrega Pendente -> {Style.RESET_ALL}{Fore.BLUE}{msg[3]}{Style.RESET_ALL}
{'=' * 100}
"""
        print(output)

    def show_input(self, texto:str):
       return input(
        f"{'*' * 100}\n{Back.BLACK}{Style.BRIGHT}{Fore.GREEN}{texto}{Style.RESET_ALL} {Fore.GREEN}{Style.RESET_ALL}".center(100)
    )
    def fail_find(self, texto:str):
       print(
        f"{'*' * 106}\n{Back.BLACK}{Style.BRIGHT}{Fore.GREEN}{texto}{Style.RESET_ALL} {Fore.GREEN}{Style.RESET_ALL}".center(100)
    )



