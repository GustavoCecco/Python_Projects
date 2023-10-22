# Funcionalidade
O código importa o módulo datetime do Python para lidar com datas e tempo.

O usuário é solicitado a digitar um objetivo com um prazo separado por dois pontos. A entrada é então dividida em uma lista usando o caractere ":" como separador.

A primeira parte da lista (input_list[0]) é atribuída à variável goal, que representa o objetivo informado pelo usuário.

A segunda parte da lista (input_list[1]) é atribuída à variável deadline, que representa a data de prazo informada pelo usuário.

O código utiliza a função strptime do módulo datetime para converter a string da data de prazo em um objeto datetime. O formato da data esperado é "dia.mês.ano" (por exemplo, "25.12.2023").

A variável today_date é definida como o objeto datetime representando a data atual.

Em seguida, a diferença entre a data de prazo e a data atual é calculada, resultando em um objeto timedelta que representa o tempo restante até a data de prazo.

Por fim, o tempo restante é impresso na saída padrão, exibindo o objetivo e a quantidade de dias restantes até a data de prazo.

## Executando o Projeto

Para executar o projeto, basta executar o arquivo Python contendo o código. O programa solicitará que o usuário digite um objetivo com um prazo separado por dois pontos. Em seguida, exibirá o tempo restante em dias até a data de prazo.

Certifique-se de ter o Python instalado em sua máquina para executar o projeto. Você pode executar o programa através do comando python nome_do_arquivo.py no diretório do projeto.
