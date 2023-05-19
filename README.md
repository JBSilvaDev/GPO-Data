# Documentação
## Descrição do Projeto
  - O projeto consiste em um programa que obtém informações relacionadas a uma PEC por meio do sistema GPO (Gestão portuaria) utilizando web scraping. O programa exibe as informações no terminal.

## Arquivos do Projeto
  - O projeto é composto pelos seguintes arquivos:

>`main.py`
  - Este é o arquivo principal do projeto. Ele contém a função main() que é responsável por controlar o fluxo do programa. A função inicia uma instância do GpoController e ShowInfoTerminal, exibe um prompt para digitar o número da PEC e obtém as informações correspondentes. O programa continua em um loop até que o usuário digite 'q' para sair.

>`show_info_terminal.py`
  - Este arquivo contém a classe ShowInfoTerminal, responsável por exibir as informações no terminal. Possui métodos para exibir uma lista de itens de PEC, solicitar uma entrada de texto e exibir uma mensagem de falha.

>`browser.py`
  - O arquivo browser.py contém a classe BrowserController, que é uma classe base para controle do navegador. É utilizada como classe pai pela classe GpoController para encapsular a lógica de controle do navegador. Ele usa a biblioteca Selenium para interagir com o navegador Chrome.

>`gpo_controller.py`
 - O arquivo gpo_controller.py contém a classe GpoController, responsável por obter informações do sistema GPO. Ela herda da classe BrowserController e inclui métodos para realizar o login no sistema, obter informações de PR/Vão e outras informações relacionadas à PEC.

>`gpo_model.py`
  - Este arquivo armazena as informações do site de acesso, como links e credenciais de acesso ao sistema GPO. No código fornecido, ele é importado

## Fluxo de Execução
  - O programa inicia executando a função main() em `main.py`.
  - É criada uma instância do GpoController e do ShowInfoTerminal.
  - O programa entra em um loop infinito.
  - O usuário é solicitado a digitar o número da PEC.
  - Se o usuário digitar 'q', o programa exibe uma mensagem de encerramento e sai do loop.
  - Caso contrário, o programa exibe uma mensagem indicando que está aguardando retorno.
  - O GpoController é usado para obter as informações de PR/Vão e outras informações relacionadas à PEC.
  - O programa exibe as informações no terminal usando a classe ShowInfoTerminal.
  - O programa repete o loop para solicitar uma nova entrada do usuário.
  - Quando o usuário digitar 'q', o programa encerra, fecha o navegador e exibe uma mensagem de encerramento final.
### Requisitos de Dependência
  - O projeto possui as seguintes dependências que devem ser instaladas para executá-lo corretamente:
    - halo: Biblioteca para exibir spinners no terminal.
    - colorama: Biblioteca para estilização de cores no terminal.
    - selenium: Biblioteca para automação de navegador.
    - Certifique-se de ter as dependências instaladas antes de executar o projeto.

## Executando o Projeto
  - Certifique-se de ter o Chrome instalado em seu sistema, pois o projeto utiliza o ChromeDriver para controlar o navegador Chrome.
  - Execute o arquivo main.py para iniciar o programa.
  - Digite o número da PEC quando solicitado e pressione Enter.
  - O programa exibirá as informações da PEC no terminal.
  - Repita o passo 4 para consultar outras PECs.
  - Quando desejar sair do programa, digite 'q' e pressione Enter.