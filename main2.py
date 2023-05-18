# Importações necessárias
from controller.gpoController.gpo_controller import GpoController


# Cria uma instância do GpoController
gpo_controller = GpoController()

# Loop principal
while True:
    # Obtém o número de PEC do usuário
    pec_numero = input("Digite o número da PEC (ou 'q' para sair): ")
    
    # Verifica se o usuário deseja encerrar o programa
    if pec_numero.lower() == "q":
        break
    
    # Cria uma variável para armazenar os valores de PR e VÃO
    text_info_pr_vao= gpo_controller.getPrVao(pec_numero)
    
    # Exibe os valores de PR e VÃO na tela
    if text_info_pr_vao:
        print(text_info_pr_vao)
    else:
        print("Não foi possível obter as informações.")

# Encerra o programa
print("Encerrando o programa.")
