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

# Explicando o código

1. **Importação do módulo `openpyxl`**

   ```python
   import openpyxl
   ```

   O código começa importando o módulo `openpyxl`, que é uma biblioteca em Python usada para trabalhar com arquivos do Microsoft Excel (formato xlsx). Essa biblioteca permite ler, escrever e manipular dados em planilhas.

2. **Carregando o arquivo de planilha**

   ```python
   inv_file = openpyxl.load_workbook("inventory.xlsx")
   product_list = inv_file["Sheet1"]
   ```

   Aqui, o código carrega o arquivo de planilha chamado "inventory.xlsx" usando a função `openpyxl.load_workbook()`. Em seguida, ele acessa a planilha com o nome "Sheet1" usando a sintaxe de dicionário. A variável `product_list` agora contém uma referência à planilha que será usada para extrair e atualizar dados.

3. **Inicialização de dicionários**

   ```python
   products_per_supplier = {}
   total_value_per_supplier = {}
   products_under_10_inv = {}
   ```

   O código cria três dicionários vazios: `products_per_supplier`, `total_value_per_supplier` e `products_under_10_inv`. Esses dicionários serão usados para armazenar informações relevantes sobre os produtos e as empresas fornecedoras.

4. **Iteração pelas linhas da planilha**

   ```python
   for product_row in range(2, product_list.max_row + 1):
       # Código para processar cada linha da planilha aqui
   ```

   O código utiliza um loop `for` para iterar pelas linhas da planilha, começando da linha 2 (para evitar o cabeçalho) até a última linha (`product_list.max_row + 1`). Em cada iteração, ele processará as informações de um produto específico.

5. **Extraindo informações do produto**

   ```python
   supplier_name = product_list.cell(product_row, 4).value
   inventory = product_list.cell(product_row, 2).value
   price = product_list.cell(product_row, 3).value
   product_num = product_list.cell(product_row, 1).value
   inventory_price = product_list.cell(product_row, 5)
   ```

   Nesta parte, o código extrai informações específicas de cada célula da linha atual da planilha. Ele obtém o nome do fornecedor (`supplier_name`), a quantidade em estoque (`inventory`), o preço do produto (`price`) e o número do produto (`product_num`). A variável `inventory_price` é uma referência à célula onde o valor total do inventário será armazenado.

6. **Cálculo do número de produtos por fornecedor**

   ```python
   if supplier_name in products_per_supplier:
       current_num_products = products_per_supplier.get(supplier_name)
       products_per_supplier[supplier_name] = current_num_products + 1
   else:
       products_per_supplier[supplier_name] = 1
   ```

   Nesta parte, o código realiza o cálculo do número de produtos por fornecedor. Ele verifica se o nome do fornecedor (`supplier_name`) já existe no dicionário `products_per_supplier`. Se sim, ele recupera o valor atual (o número de produtos já contados) e incrementa 1 para representar o novo produto. Se o fornecedor ainda não existe no dicionário, é adicionado com o valor 1 (indicando o primeiro produto).

7. **Cálculo do valor total do inventário por fornecedor**

   ```python
   if supplier_name in total_value_per_supplier:
       current_total_value = total_value_per_supplier.get(supplier_name)
       total_value_per_supplier[supplier_name] = current_total_value + inventory * price
   else:
       total_value_per_supplier[supplier_name] = inventory * price
   ```

   Aqui, o código realiza o cálculo do valor total do inventário por fornecedor. Ele verifica se o nome do fornecedor (`supplier_name`) já existe no dicionário `total_value_per_supplier`. Se sim, ele recupera o valor atual (o valor total do inventário já calculado) e soma o valor do inventário atual (`inventory * price`). Se o fornecedor ainda não existe no dicionário, é adicionado com o valor `inventory * price`.

8. **Identificação de produtos com estoque menor que 10**

   ```python
   if inventory < 10:
       products_under_10_inv[int(product_num)] = int(inventory)
   ```

   Aqui, o código verifica se o estoque (`inventory`) de um produto é menor que 10. Se for verdadeiro, o número do produto (`product_num`) e o estoque atual são adicionados ao dicionário `products_under_10_inv`. Esse dicionário será usado para listar os produtos com estoque menor que 10.

9. **Atualização do valor do inventário na planilha**

   ```python
   inventory_price.value = inventory * price
   ```

   O código atualiza o valor da célula `inventory_price` na planilha com o valor total do inventário do produto atual. Isso é calculado multiplicando a quantidade em estoque (`inventory`) pelo preço do produto (`price`).

10. **Impressão dos resultados**

    ```python
    print(products_under_10_inv)
    print(products_per_supplier)
    print(total_value_per_supplier)
    ```

    Por fim, o código imprime os resultados obtidos após o processamento da planilha. Ele exibirá os produtos com estoque menor que 10, a contagem de produtos por fornecedor e o valor total do inventário para cada fornecedor.

11. **Salvando a planilha atualizada**

    ```python
    inv_file.save("inventory_with_total_value.xlsx")
    ```

    O código salva a planilha atualizada com os valores do inventário na célula correspondente em um novo arquivo chamado "inventory_with_total_value.xlsx".
