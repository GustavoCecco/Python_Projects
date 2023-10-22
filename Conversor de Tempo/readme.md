# Módulos

### Main
O módulo main contém o código principal do programa. Ele importa duas funções do módulo helper: validate_and_execute e user_input_message. O código é responsável por solicitar ao usuário que insira o número de dias e a unidade de conversão repetidamente até que o usuário digite "exit" para sair.

O programa divide a entrada do usuário em dias e unidade, cria um dicionário days_and_units_dictionary e chama a função validate_and_execute passando esse dicionário como argumento.

### Helper
O módulo helper contém as funções auxiliares para o processamento e cálculos do programa.

A função days_to_units recebe o número de dias e a unidade de conversão e retorna uma string com o valor convertido. Ela realiza os cálculos para converter os dias em horas ou minutos, dependendo da unidade especificada.

A função validate_and_execute recebe um dicionário days_and_units_dictionary contendo os dias e a unidade de conversão. Ela valida se o número de dias é um valor válido (maior que zero) e chama a função days_to_units para realizar a conversão. O resultado é exibido na saída padrão.

## Executando o Projeto

Para executar o projeto, basta executar o módulo main. O programa solicitará que o usuário insira o número de dias e a unidade de conversão desejada. Os resultados da conversão serão exibidos no console.

Certifique-se de ter o Python instalado em sua máquina para executar o projeto. Você pode executar o programa através do comando python main.py no diretório do projeto.

Divirta-se utilizando o Conversor de Tempo!
