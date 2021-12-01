## Knn_desenvolvimento

K-Nearest Neighbors - KNN
Modelo supervisionado de machine learning que pode ser utilizado tanto para classificação, isto é, rotular os dados; quanto para regressão, ou seja, aproximar valores.

Características:
-Dependendo da implementação pode ser  𝑂(𝑛∗𝑚)  ou  𝑂(𝑙𝑜𝑔(𝑛)) 
-Simples
-Interpretável
-Largamente conhecido e estudado
-Razoavelmente rápido
-Por conta disso é um ótimo benchmark

Algoritmo:
-Passo 1: Definir um valor para K
-Passo 2: Definir os K vizinhos mais próximos do ponto a ser classificado de acordo com uma função de distância.
-Passo 3:
 Se for um problema de Regressão: Calcular a média de todos os vizinhos.
 Se for um problema de Classificação: Calcular a moda de todos os vizinhos.
 Passo 4: Atribuir o valor/classe ao ponto de interesse conforme cálculo do Passo 3.

Definição do Problema

Dados

Os dados abaixo são referentes ao cadastro de clientes de uma empresa de investimentos com suas respectivas carteira de investimentos, que indica se esse cliente tem o perfil de investidor Conservador, Moderado ou Agressivo. O nosso intuito é, a partir do investimento de alguns clientes que já tem um perfil definido, estimar esse perfil para aqueles que ainda não estão classificado, afim de oferecer novos produtos que sejam mais adequados a eles.

Os dados abaixo seguem o seguinte padrão:

[CPF: INT, Perfil Do Investidor: STRING, Carteira de Investimento: TUPLA]

Regras

Se você precisar de uma função para computar algo crie ela
Não é permitido usar nenhum módulo externo como numpy e math
Use apenas os objetos e fluxos visto até o momento no curso