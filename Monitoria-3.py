# -*- coding: utf-8 -*-
"""
Monitoria 3 de Macroeconomia I (Parte 1) de 2021
04/05/2021 - author: Fábio Nishida

Baseado no curso "Introdução à Ciência da Computação com Python Parte 2"
de Fabio Kon (IME-USP) no Coursera (gratuitos para visualização)
https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2

Caso tenha interesse, comunidade USP pode pegar o certificado sem pagar os cursos:
https://jornal.usp.br/universidade/nova-parceria-oferece-mais-cursos-on-line-a-comunidade-usp-na-plataforma-coursera/
"""

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

[A[0][1]] + [A[1][1]] + [A[2][1]]  # 2ª coluna da matriz
# pega o elemento da 2ª coluna de cada linha, transforma em lista e "soma" (listas)


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


# Para criar uma matriz "vazia" (com zeros), usa-se a função zeros() do NumPy
B = np.zeros([5, 8])
print(B)
type(B)


# Para saber as dimensões de uma matrix usamos a função len()
len(B)  # Número de linhas de B
len(B[0])  # Número de elementos na 1ª linha de B (ou seja, número de colunas)


# Usando Módulo NumPy
# usando matriz (lista de listas) padrão
matriz_lista = [[1, 2, 3],
                [2, 3, 1]]
matriz_lista * 2
matriz_lista + 2

# usando matriz convertida para formato array
matriz_array = np.array(matriz_lista)
type(matriz_array)

matriz_array * 2
matriz_array + 2


# Criar sequência de números usando linspace do NumPy
sequencia = np.linspace(0, 1, 10)
type(sequencia)

# Criar números aleatórios usando do NumPy
aleatorio = np.random.uniform(0, 1, size = 10)
type(aleatorio)

np.random.normal(0, 1, size = 10)



##############################################################################
""" REPETIÇÃO / LOOP USANDO FOR """
# Na repetição utilizando "for", criamos/atualizamos uma variável que percorre
# todos os elementos/objetos de uma lista.

# Repetição usando "for"
for i in [1, "oi", 7, 99.2]:
    print(i)

i  # Note que i se mantém no último valor após acabar o loop


# Criação de uma lista com sequência de números
?range  # Para visualizar ajuda do comando: range(start, stop[, step])
# Se preencher apenas um argumento de range(), começa no 0 e termina no nº - 1
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


# Exemplo de preenchimento de matrizes - Tabela da Tabuada
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


# Comparando ambas matrizes
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
fibonacci(4)


# Note que o uso de função para solucionar essas recursões pode não ser o mais
# eficiente, pois cada vez que a função é "chamada" parte-se do caso base para
# fazer o cálculo do n desejado. Durante o curso, vamos resolver por loops.


# Exemplo: Calcular o primeiro valor n cujo fibonacci ultrapassa 15 milhões
# Via função (~ 18 segundos de execução)
n = 1
while fibonacci(n) < 15_000_000:  # Cada loop calcula desde a base da recursão
    n += 1

print(n)


# Via loop (instantâneo)
n = 2  # Estabelecendo a base da recursão
fibonacci_n_1 = 1
fibonacci_n_2 = 1

while fibonacci_n_1 + fibonacci_n_2 < 15_000_000:  # Usa cálculos anteriores
    auxiliar = fibonacci_n_2
    fibonacci_n_2 = fibonacci_n_1
    fibonacci_n_1 = fibonacci_n_1 + auxiliar
    n += 1

print(n)



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
