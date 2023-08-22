# Projeto Airbnb Rio - Ferramenta de Previsão de Preço de Imóvel para Pessoas Comuns

## Contexto
No Airbnb, qualquer pessoa que tenha um quarto ou um imóvel de qualquer tipo (apartamento, casa, chalé, pousada, etc.) pode ofertar o seu imóvel para ser alugado por diária. Ao criar o perfil de anfitrião, que é a pessoa que disponibiliza um imóvel para aluguel por diária, é necessário criar um anúncio detalhado do imóvel. Nesse anúncio, informações sobre as características do imóvel são fornecidas para ajudar locatários/viajantes a escolherem a melhor opção.
Existem várias personalizações possíveis no anúncio, como quantidade mínima de diárias, preço, número de quartos, regras de cancelamento, taxa extra para hóspedes extras, entre outras.

## Objetivo
O objetivo deste projeto é construir um modelo de previsão de preços de imóveis para permitir que pessoas comuns que possuem imóveis saibam quanto cobrar pela diária de suas propriedades. Além disso, o modelo pode ajudar locatários comuns a determinar se um imóvel está com um preço atrativo em comparação com propriedades semelhantes.

## Dados 
Os dados utilizados para esse projeto foram obtidos a partir do site Kaggle, especificamente o dataset "Airbnb Rio de Janeiro". O dataset contém informações sobre os preços dos imóveis e suas características, abrangendo o período de abril de 2018 a maio de 2020, exceto junho de 2018.

Para referência e insights, a solução do usuário Allan Bruno no Kaggle também foi consultada: [Notebook de referência do Kaggle](https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb)

## Etapas do Projeto
**Importação e Tratamento dos Dados:** As bases de dados foram coletadas e integradas, criando colunas de mês e ano. Em seguida, as colunas irrelevantes para o modelo foram eliminadas, e valores faltantes foram tratados.

**Análise Exploratória e Tratamento de Outliers:** Foram realizadas análises e tratamentos das colunas de valores numéricos, como preço, acomodações, quartos, banheiros, entre outros. Outliers foram identificados e, quando apropriado, removidos. Algumas colunas foram excluídas quando não contribuíram para o modelo.

**Tratamento de Colunas de Valores Textuais:** As colunas de valores categóricos e de valores booleanos foram tratadas, convertendo-as para formatos mais adequados para a modelagem. Além disso, foi realizada uma análise e agrupamento de valores menos frequentes em algumas colunas categóricas.

**Codificação e Modelagem:** As colunas de valores booleanos foram codificadas para valores numéricos, e colunas categóricas foram transformadas em variáveis dummy. Três modelos de regressão (Random Forest, Linear Regression e Extra Trees) foram escolhidos e treinados para prever os preços dos imóveis.

**Avaliação e Escolha do Melhor Modelo:** Os modelos foram avaliados com base nas métricas R² e RMSE (Root Mean Squared Error). O modelo Extra Trees se destacou como o mais adequado, com alto valor de R² e baixo valor de RMSE.

**Ajustes Finais:** Foram realizados ajustes finais no modelo vencedor, incluindo a remoção de features menos relevantes. O modelo foi testado novamente para verificar a melhoria nas métricas.

## Resultados
O modelo Extra Trees se mostrou eficaz na previsão de preços de imóveis com base nas características fornecidas. Ele foi escolhido como o melhor modelo devido aos altos valores de R² (97.49%) e ao baixo valor de RMSE (41.99). Os recursos mais relevantes para a previsão de preços foram identificados por meio de uma análise de importância de recursos.

## Deploy do Projeto
Para disponibilizar o modelo para uso prático, ele pode ser salvo usando a biblioteca joblib. Existem várias opções para o deploy, como a criação de um arquivo executável com Tkinter, um microsite com Flask ou uma interface no formato de aplicativo móvel.

## Benefícios
O projeto traz diversos benefícios:

**Facilidade para Anfitriões:** Anfitriões comuns que desejam alugar seus imóveis no Airbnb podem utilizar o modelo para definir preços competitivos e atrativos.

**Auxílio para Viajantes:** Pessoas que desejam alugar imóveis para temporada no Rio de Janeiro podem avaliar se o preço pedido é justo com base nas características da propriedade.

**Otimização de Ocupação:** O modelo pode ajudar anfitriões a otimizar a ocupação de seus imóveis, ajustando os preços de acordo com a demanda e a concorrência.

**Referência para Decisões:** Mesmo para quem não pretende alugar no Airbnb, o modelo pode servir como referência na avaliação do valor de imóveis com base em suas características.

## Conclusão
O projeto "Airbnb Rio - Ferramenta de Previsão de Preço de Imóvel para Pessoas Comuns" construiu com sucesso um modelo de previsão de preços de imóveis eficaz. Com um modelo treinado e ajustado, anfitriões e locatários comuns podem tomar decisões mais informadas sobre os preços de aluguel, gerando benefícios para ambos os lados do mercado.
