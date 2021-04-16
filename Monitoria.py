# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 22:18:10 2021
@author: Fábio Nishida

Baseado no curso "Introdução à Ciência da Computação com Python Partes 1 e 2"
de Fabio Kon (IME-USP) no Coursera (gratuitos para visualização)
https://www.coursera.org/learn/ciencia-computacao-python-conceitos
https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2

Caso tenha interesse, comunidade USP pode pegar o certificado sem pagar o curso:
https://jornal.usp.br/universidade/nova-parceria-oferece-mais-cursos-on-line-a-comunidade-usp-na-plataforma-coursera/
"""


##############################################################################
""" OPERAÇÕES BÁSICAS """
# Soma e Subtração
1 + 1
2 - 3

# Multiplicação e Divisão
2 * 3
6 / 4

# Divisão Inteira e Resto da Divisão
6 // 4
6 % 4

# Potenciação
2 ** 3
8 ** (1 / 3)


# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/N1e0Z/tipos-de-dados



##############################################################################
""" ALGUNS ATALHOS NO SPYDER """
# Rodar única linha: Selecionar a linha (ou realçá-la inteira) + F9
2 + 1 * 3 - 4 ** 2
# É possível rodar apenas parte do código, selecionando parte da linha
# Teste na linha de código acima, rodar apenas "2 + 1 * 3 - 4" (igual a 1)

# Rodar várias linhas: Realçar várias linhas + F9
2 ** 3
8 ** (1 / 3)



##############################################################################
""" Comentários no Código """
# Para incluir comentário no código, é possível fazê-lo por
#   • 3 aspas de cada lado: comentário fica destacado em verde
#       (Ao digitar 4 aspas seguidas, aparecerá 6 aspas e cursor fica no meio)
#   • Incluir # antes do código (ou Ctrl + 1): pode ser depois de um comando
2 ** 3 # 2 ao cubo

# IMPORTANTE: Sempre deixe comentários para lembrar posteriormente o que feito
# e, caso o código seja compartilhado, outros possam entender.



##############################################################################
""" ATRIBUIÇÕES A VARIÁVEIS / OBJETOS """
# Criando novas variáveis / objetos
x = 5
x
type(x)  # Objeto "x" é um integer (inteiro)

y = 10 / 3  # Usa-se o ponto como separador decimal
y
type(y)  # Objeto "y" é um float (um dos tipos de números reais)


# Alterando valores
x = 345
x

# É possível atribuir novo valor alterando o antigo
x = x + 20
x

# Também pode ser escrito como:
x += 20  # Pode-se usar outros operadores: "-", "*", "/", "**"
x


# Soma de variáveis (seus tipos precisam ser consistentes entre si)
soma = x + y
soma
type(soma)


# NESTE CASO, ao alterarmos o valor de "x" após criar "soma", não altera "soma"
x
x *= 2
x
soma

# Quando lidarmos com matrizes e fizermos alterações em seus elementos,
# precisaremos lidar de outra forma.


# Variáveis com textos
palavra = "Olá"  # Também pode ser com aspas simples: 'Olá'
palavra
type(palavra)  # Objeto é um string (texto)
len(palavra)  # Tamanho do string

# Concatenação de texto com números
print("A soma é", round(soma, 1))  # Já inclui espaçamento entre os argumentos
# round() foi usado para arredondar "soma" com 1 casa decimal



##############################################################################
""" EXPRESSÕES BOOLEANAS """
2 < 20
5 <= 4
10 > 5
19 >= 19

100 == 10 ** 2
100 != 10 * 5
not 100 == 10 * 5

type(100 == 10 ** 2)  # Objeto boolean tem 2 valores: TRUE ou FALSE (1 ou 0)

# Erro! O símbolo de "=" é uma forma de ATRIBUIÇÃO de valor a uma variável
10 = 10

# Objeto boolean pode ser aplicado a uma variável também
idade = 15
maioridade = 18
pode_dirigir = idade >= maioridade
pode_dirigir
type(pode_dirigir)


# Expressões Compostas
x = 200
x < 0 or x ** 2 > 100
x < 0 and x ** 2 > 100


not x < 0 and x ** 2 > 100  # "not" nega apenas a primeira expressão
not (x < 0 and x ** 2 > 100)  # "not" nega tudo em parêntesis

# Mesmo que redundante, colocar parêntesis pode ajudar na leitura do código
(not x < 0) and x ** 2 > 100

# Tabela de Precedência de Operadores
# Nível 7 - exponenciação: **
# Nível 6 - multiplicação: *, /, //, %
# Nível 5 - adição: +, -
# Nível 4 - relacional: ==, !=, <=, >=, >, <
# Nível 3 - lógico: not
# Nível 2 - lógico: and
# Nível 1 - lógico: or


# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/40vwN/expressoes-booleanas



##############################################################################
""" EXECUÇÃO CONDICIONAL """
x = -1
if x < 0:
    print("número negativo")
# ATENÇÃO: comando decorrente do "if" deve ter algum indentação (tabulação)
# em relação ao comando de execução condicional. O padrão são 4 espaços a mais.
# Para rodar com a condicional, precisa realçar as 2 linhas antes de executar.


# Incluindo comando "else", caso a condição seja falsa
x = 1
if x < 0:
    print("número negativo")
else:
    print("zero ou número positivo")
# Note que o "else" é escrito sem indentação


# Incluindo mais possíveis condições
x = 0
if x < 0:
    print("número negativo")
elif x == 0: # elseif
    print("zero")
else:
    print("número positivo")
    
# ou também, pode incluir mais uma condicional dentro (cuidado com indentação!)
x = 0
if x < 0:
    print("número negativo")
else:
    if x > 0:
        print("número positivo")
    else:
        print("zero")
        
        
# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/1cG2Z/execucao-condicional


# EXERCÍCIO: Calcular raízes reais pela fórmula de Bháskara
# Considerar casos em que delta é positivo, zero ou negativo (sem raízes reais)
# Testar para os casos:
#   • a = 10, b = 25, c = 10
#   • a = 10, b = 20, c = 10
#   • a = 10, b = 10, c = 10
# https://www.coursera.org/learn/ciencia-computacao-python-conceitos/lecture/KSJBH/exercicio-resolvido
# *não precisa usar o "input", pode inserir o valor a "a", "b" e "c" diretamente
# *para a raiz quadrada, pode usar "** (1/2)"



##############################################################################
""" CRIAÇÃO DE FUNÇÕES """
# Útil para evitar repetições de grandes blocos de comandos no programa

# Função simples de soma de dois inputs
def soma(a, b):  # Exigindo 2 argumentos
    return a + b

soma(15, 46)
soma(5, 82)


# Função não necessariamente precisa ter algum input
def mensagem():
    return print("Olá")

mensagem()


# Exemplo de cálculo de temperatura
temperaturaFarenheit = 68 
temperaturaCelsius = (temperaturaFarenheit - 32) * 5 / 9
temperaturaCelsius

# Criação de uma função com o cálculo anterior, com um parâmetro
def Calcular_Temperatura_Celsius(tempFarenheit):
    return (tempFarenheit - 32) * 5 / 9

# tempFarenheit é uma variável "temporária" que só funcionada dentro da função
# e o seu valor vai ser inserido ao digitar o comando (ver abaixo).
# "return" é o comando para dizer qual é o ouput desta função (graus Celsius)

Calcular_Temperatura_Celsius(68)
Calcular_Temperatura_Celsius(86)


# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/exam/mJrGn/funcoes



##############################################################################
""" REPETIÇÃO / LOOP USANDO WHILE """
# Na repetição utilizando "while", precisamos criar uma variável (indicador de 
# passagem) antes que servirá para criarmos as expressões condicionais.

i = 0 # indicador de passagem
while i <= 10:
    print(2 ** i)
    i += 1  # Equivalente a i = i + 1
# ATENÇÃO: não se esqueça de acrescentar unidades em cada loop


# No exemplo abaixo, a condição sempre será verdadeira: nunca terminará o loop
i = 0
while i > -1:
    print(2 + i)
    i += 1  # Equivalente a i = i + 1
# Para parar o loop, clique no quadrado do lado esquerdo -->


# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/moDKn/repeticao-com-while


# Exemplo 1: achar a temperatura em Farenheit equivalente/próxima a 35ºC
# (usar a função Calcular_Temperatura_Celsius criada dentro de um loop)
temperaturaFarenheit = 0
while Calcular_Temperatura_Celsius(temperaturaFarenheit) < 35:
    temperaturaFarenheit += 1
    
print(temperaturaFarenheit, "graus Farenheit é equivalente a",
      Calcular_Temperatura_Celsius(temperaturaFarenheit), "graus Celsius")


# Exemplo 2: suponha que a vacinação começará agora e a cada mês é possível
# Vacinar 10% das pessoas ainda não vacinadas, em quantos meses é possível
# Vacinar toda população?
perc_pop_nao_vacinada = 1
meses = 1

while perc_pop_nao_vacinada > 0:
    perc_pop_nao_vacinada *= 0.9  # Equivalente a perc_pop_nao_vacinada = perc_pop_nao_vacinada * 0.9
    meses += 1
print(meses)

# Note que o percentual se aproxima de zero, mas nunca será zero, então podemos
# estabelecer % da população que seria razoável considerar como "toda população"
# Digamos que esse percentual seja 99,9%
perc_pop_nao_vacinada = 1
meses = 1
tolerancia = 0.01

while perc_pop_nao_vacinada > tolerancia:
    perc_pop_nao_vacinada = perc_pop_nao_vacinada * 0.9
    meses += 1
print("São necessários", meses, "meses para vacinar toda população")



##############################################################################
""" LISTAS """
# também chamado de coleção de objetos, vetor, array

lista = [1, 2, 3, 4, 5]
lista
len(lista)  # Comprimento (length) da lista

lista[0]  # Numeração começa no zero!
lista[4]  # 5º elemento da lista


# para acrescentar um novo elemento, usa-se ".append"
lista2 = []  # Lista vazia
lista2.append("oi")
len(lista2)  # Contém 1 elemento
lista2[0]  # 1º elemento


# Dentro de uma lista, pode ter elementos de tipos distintos
filme = ["O que é isso companheiro?", "Bruno Barreto", 1.83, 1997]
type(filme) # list
type(filme[0])  # string
type(filme[1])  # string
type(filme[2])  # float
type(filme[3])  # integer


# É possível alterar os valores dos objetos
filme[3] = 2001
filme

# É pouco usual, mas é possível utilizar valores negativos para se referir aos
# objetos do final para o início
filme[-1] = 1997
filme


# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/ArJZT/listas



##############################################################################
""" MANIPULAÇÃO DE LISTAS """
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
len(primos)

primos[1:2]  # Note que traz um único elemento (é subtraído 1 do último nº)
primos[1:4]  # Traz 3 elementos (é subtraído 1 do último nº)

# Dividindo pela metade
primos[0:int(len(primos)/2)]  # Aqui int() transforma número float em integer
primos[int(len(primos)/2):len(primos)]

# números iniciais e finais não precisavam ser informados
primos[:int(len(primos)/2)]
primos[int(len(primos)/2):]


# Clonando listas - CUIDADO!
# Ao clonar objetos e depois alterar um objeto original, não altera valor do clonado
a = 3
b = a
a
b

a = 5
a
b


# Mas isto NÃO É VÁLIDO para LISTAS - os objetos continuam referenciados
lista1 = ["vermelho", "verde", "azul"]
lista2 = lista1
lista1
lista2

lista1[0] = "rosa"
lista1
lista2  # lista2 também mudou ao alterar apenas a lista1!

lista2[1] = "roxo"
lista1  # Se altero lista2, também altero lista1!
lista2 


# Clonar listas corretamente (objeto por objeto) criando uma nova função
def clone(lista):
    clone = []
    for objeto in lista:
        clone.append(objeto)
    return clone

lista1 = ["vermelho", "verde", "azul"]
lista2 = clone(lista1)
lista1
lista2

lista1[0] = "rosa"
lista1
lista2  # Manteve-se no formato original


# Há uma maneira mais simples que é indicando todos elementos da lista 1
lista1 = ["vermelho", "verde", "azul"]
lista2 = lista1[:]  # Indicando todos elementos da lista1
lista1
lista2

lista1[0] = "rosa"
lista1
lista2  # Manteve-se no formato original


# Pertencimento a uma lista
"rosa" in lista1
"rosa" in lista2


# Repetição de Listas
primos
primos * 2  # Não multiplica por 2 os valores, duplica o tamanho da lista

lista1
lista1 * 3


# Soma de listas
carnes1 = ["picanha", "alcatra"]
carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
carnes3 = carnes2 + carnes1


# Remoção de objetos em listas
lista1
del lista1[1]
lista1


# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/Uw2C6/manipulacao-de-listas



##############################################################################
""" IMPORTAÇÃO DE MÓDULOS / PACOTES """
# Importação do pacote "math"
import math
# https://docs.python.org/3/library/math.html

# Para usar uma função, é necessário escrever o nome do módulo antes da função
math.exp(1)
exp(9)  # Erro!


# Importação do pacote "numpy": pacote que mais utilizado na disciplina
# https://medium.com/ensina-ai/entendendo-a-biblioteca-numpy-4858fde63355
import numpy as np # pode dar um apelido para não ter que escrever o nome inteiro

A = np.array([1, 5, 7, 4])
print(A)  # Para visualizar matrizes/vetores é melhor usar o print()
numpy.array([1, 5]) # Erro!


# Importação de apenas uma função de um módulo, sem ter que escrever o módulo
from math import log as log
log(math.exp(1))



##############################################################################
""" MATRIZES (LISTA DE LISTAS) """

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]  # Note que estamos criando listas dentro de uma lista
A

# Formas de "chamar" parte da matriz
A[0][0]  # 1ª linha e 1ª coluna
A[2][2]  # 3ª linha e 3ª coluna

A[0]  # 1ª linha da matriz
A[0][:]  # 1ª linha da matriz

A[:][1]  # 2ª coluna da matriz

# Criação de matriz vazia
def cria_matriz(num_linhas, num_colunas, valor):
    """ (int, int, valor) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_coluna colunas
    em que cada elemento é igual ao valor dado.
    """
    matriz = []
    for i in range(num_linhas):
        # cria linha i
        linha = [] # lista vazia
        for j in range(num_colunas):
            linha.append(valor)
        
        # adiciona linha à matriz
        matriz.append(linha)
    
    return matriz

cria_matriz(5, 8, 0)


# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2/quiz/QUA4k/matrizes


# Uma outra forma de criar matriz é por meio do módulo NumPy
# Utiliza as listas no formato "array", que é mais eficiente e facilita operações
# https://www.geeksforgeeks.org/python-lists-vs-numpy-arrays/

# Para criar uma matriz no formato array usa-se a função "array" do NumPy
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]) 
A
print(A)  # Matriz em array é melhor visualizada usando print()
type(A)

# A sintaxe do array é diferente: apenas [,] (ao invés de [][])
A[0, 0]  # 1ª linha e 1ª coluna
A[2, 2]  # 3ª linha e 3ª coluna

A[0]  # 1ª linha da matriz
A[0, :]  # 1ª linha da matriz

A[:, 1]  # 2ª coluna da matriz


# Para criar uma matriz "vazia" (preenchida por zeros), usar-se o zeros() do NumPy
B = np.zeros([5, 8])
print(B)
type(B)


# Para saber as dimensões de uma matrix usamos a função len()
len(B)  # Número de linhas de B
len(B[0])  # Número de elementos na 1ª linha de B (ou seja, número de colunas)


# Operações NumPy
# usando matriz (lista de listas) padrão
matriz_lista = [[1, 2, 3],
                [2, 3, 1]]
matriz_lista * 2
matriz_lista + 2

# usando matriz convertida para formato array
matriz_array = np.array(lista)
matriz_array * 2
matriz_array + 2



##############################################################################
""" REPETIÇÃO / LOOP USANDO FOR """
# Na repetição utilizando "for", criamos/atualizamos uma variável que percorre
# todos os elementos/objetos de uma lista.

del i  # Deletar a variável i utilizada em outro exemplo (acima)
i  # Apenas para verificar que for realmente deletada

# Repetição usando "for"
for i in [1, "oi", 7, 99.2]:
    print(i)

i  # Note que i se mantém o último valor após acabar o loop


# Criação de uma lista com sequência de números
?range  # Para visualizar ajuda do comando: range(start, stop[, step])
# Se preencher apenas um argumento de range(), começa no 0 e termina nesse nº
# Se step for omitido, é igual a 1 (só pode ser um integer)

# função RANGE é importante para criar uma lista com números em sequência
for i in range(0, 10):
    print(i)
# Note que vai de 0 até 9 (ao invés de 10)


# Loop equivalente ao anterior, mas fazendo apenas 1 input
for i in range(10):
    print(i)
# Python adota como padrão o zero para iniciar as numerações


# Sequência de 2 em 2
for i in range(0, 10, 2):
    print(i)
# Note que não imprime o "último valor" (10)


# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/vPfhP/repeticao-com-for


##############################################################################
""" REPETIÇÕES ENCAIXADAS """
# Faremos um loop dentro de outro loop
# Preenchimento de uma matriz com a tabuada
i = 0
j = 0
while i <= 10:
    j = 0  # Precisa "resetar" a variável para o próximo loop de row
    while j <= 10:
        print(i, "-", j)
        j += 1  # Equivalente a j = j + 1
    i += 1  # Equivalente a i = i + 1 | Atenção à identação (no loop de i)


# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/QjXxx/repeticoes-encaixadas


# Exemplo de preenchimento de matrizes
# Criação de uma matriz "vazia" (com zeros)
nrow = 9  # Número de Linhas
ncol = 10  # Número de Colunas
matrix = np.zeros((nrow, ncol))
print(matrix)

# Loops para preenchimento da matriz vazia usando FOR
for lin in [[range(len(matrix)]]):
    for col in range(len(matrix[0])):
        matrix[lin, col] = (lin + 1) * (col + 1)
        
print(matrix)



# Preenchimento da matriz usando WHILE (mesma dimensão definida acima)
matrix_while = np.zeros((nrow, ncol))
print(matrix_while)

# Loops para preenchimento da matriz vazia
row = 0
col = 0
while row < nrow:
    col = 0  # Preciso "resetar" a variável para o próximo loop de row
    while col < ncol:
        matrix_while[row, col] = (row + 1) * (col + 1)
        col += 1  # Equivalente a col = col + 1
    row += 1  # Equivalente a row = row + 1 | Atenção à identação (no loop de row)
    
print(matrix_while)
matrix_while == matrix  # Comparando cada elemento das matrizes
matrix_while.all() == matrix.all()  # Comparando as matrizes como um todo



##############################################################################
""" ALGORITMOS RECURSIVOS """

# Fatorial
def fatorial(n):
    if n < 1:  # Base da recursão (caso trivial)
        return 1
    else:
        return n * fatorial(n-1)  # Chamada recursiva

fatorial(1)
fatorial(5)


# Fibonacci
def fibonacci(n):
    if n < 2:  # Base da recursão (caso trivial)
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Chamada recursiva

fibonacci(0)
fibonacci(1)
fibonacci(5)


# Busca Binária
# https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2/lecture/QSuY9/mais-sobre-recursao



##############################################################################
""" GRÁFICOS """
import matplotlib.pyplot as plt  # Módulo para fazer gráficos
import numpy as np  # Módulo para trabalhar com matrizes

# Faremos um gráfico da função y = 2^x
calculo_exponencial = np.zeros([15, 2])  # Uma coluna para x e outra para y

# Vamos preencher a matriz
for i in range(len(calculo_exponencial)):
    calculo_exponencial[i, 0] = i - 4  # Preenchendo a coluna de x (de -4 a 10)
    calculo_exponencial[i, 1] = 2 ** calculo_exponencial[i, 0]  # cálculo de y

print(calculo_exponencial)


# Criação do gráfico
fig, ax = plt.subplots()  # Cria a base (em branco) do gráfico
ax.plot(calculo_exponencial[:, 0], calculo_exponencial[:, 1],  # Coluna 0 no eixo x e coluna 1 no y
        '-o',  # Formato da linha e ponto do gráfico
        label='$y = 2^x$')  # Descrição da legenda
ax.legend()  # Faz aparecer a legenda
# ax.set_ylim([0, 1])  # tamanho mínimo e máximo vertical (corte núm. neg.)
# ax.set_xlim([-4, 0])  # tamanho mínimo e máximo horizontal (corte núm. neg.)
ax.set_xlabel('$x$')  # Descrição do eixo x
ax.set_ylabel('$y$')  # Descrição do eixo y
ax.set_title('Gráfico de $y = 2^x$')  # Título
plt.show()  # Plot do gráfico com os comandos dados



##############################################################################
""" BOAS PRÁTICAS DE PROGRAMAÇÃO EM PYTHON - PEP8 """
# https://www.coursera.org/learn/ciencia-computacao-python-conceitos/supplement/aUUua/pep8-uma-questao-de-estilo
# https://pep8.org/ (apertar Ctrl e clicar no link para acessar)

# Melhor já se acostumar a usar as boas práticas de programação enquanto está
# aprendendo a utilizar o Python.

