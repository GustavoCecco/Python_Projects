# Análise de Inventário em Python
Este projeto contém um código em Python que lida com um arquivo de planilha contendo informações de inventário de produtos. O código realiza quatro tarefas diferentes, que são explicadas em detalhes abaixo.

## Funcionalidades
1 - Listar cada empresa com a contagem de produtos respectiva
O código utiliza o módulo openpyxl para carregar o arquivo de planilha inventory.xlsx, que contém os dados do inventário dos produtos. Ele acessa a planilha "Sheet1" e, para cada linha (exceto o cabeçalho), extrai a empresa fornecedora, contando quantos produtos estão associados a cada fornecedor. O resultado é armazenado no dicionário products_per_supplier, onde a chave é o nome da empresa fornecedora e o valor é o número de produtos associados a essa empresa.

2 - Listar produtos com estoque menor que 10
Durante o processamento das linhas da planilha, o código também verifica se o estoque de um determinado produto é menor que 10. Caso seja verdadeiro, o produto é adicionado ao dicionário products_under_10_inv. Neste dicionário, a chave é o número do produto e o valor é o nível atual de estoque.

3 - Listar cada empresa com o respectivo valor total do inventário
Enquanto itera pelas linhas da planilha, o código calcula o valor total do inventário para cada empresa fornecedora. Esse cálculo é realizado multiplicando a quantidade em estoque (inventory) pelo preço do produto (price). O valor total de cada empresa é armazenado no dicionário total_value_per_supplier, onde a chave é o nome da empresa e o valor é o valor total do inventário associado.

4 - Escrever na planilha: Calcular e escrever o valor do inventário para cada produto na planilha
O código também atualiza a coluna "Inventory Value" na planilha com o valor total do inventário para cada produto. Essa informação é calculada multiplicando o estoque (inventory) pelo preço do produto (price) e armazenada na célula correspondente.

## Executando o Projeto
Para executar o projeto, basta ter o Python instalado em sua máquina, bem como a biblioteca openpyxl. O código main.py pode ser executado diretamente, e ele processará o arquivo de planilha inventory.xlsx localizado no mesmo diretório.

O programa exibirá os produtos com estoque menor que 10, a contagem de produtos por fornecedor e o valor total do inventário para cada fornecedor. Além disso, os valores do inventário serão atualizados na planilha e o resultado será salvo em um novo arquivo chamado inventory_with_total_value.xlsx.

Certifique-se de instalar o openpyxl antes de executar o programa. Você pode fazer isso através do comando pip install openpyxl.
