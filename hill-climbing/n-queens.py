"""

+ hill climbing: apresentar o número de execuções
 do programa até que uma solução seja alcançada
 (ou seja, o número de tabuleiros iniciais aleatórios
  gerados até uma solução ser encontrada) e o número
  médio de tabuleiro correntes em cada execução

+ simulated annealing: os parâmetros usados (temperatura inicial,
número máximo de iterações e alfa) que permitem encontrar
uma solução sempre que o simulated annealing é executado.

"""


import random


"""

Define o tamanho do tabuleiro

"""
board_size = 32


"""

Define a posição das rainhas em um tabuleiro,
onde o índice é a coluna do tabuleiro e o
valor é a linha em que a rainha está posicionada

"""


def generate_board(board_size):
    return [random.randint(0, board_size - 1) for i in range(board_size)]


board = generate_board(board_size)
#board = [1, 2, 3, 2]
"""
Calcula o valor do quadro atual
"""


def heuristica(board):
    h = 0
    for queen1 in range(board_size):
        for queen2 in range(queen1 + 1, board_size):
            if(board[queen1] == board[queen2]):
                h += 1
            elif(abs(queen1 - queen2) == abs(board[queen1] - board[queen2])):
                h += 1
    return h


"""
Método utilitário para calcular as heurísticas
ao mover as rainhas pelo tabuleiro e retornar as opções
"""


def calculate_neighbours(board):
    options = ['X' for a in range(board_size)]
    h_atual = heuristica(board)
    menor_valor = h_atual

    for i in range(board_size):
        row = [0 for i in range(board_size)]

        for j in range(board_size):

            if(j == board[i]):
                row[j] = 'Q'
            else:
                mock_board = [j if a == i else board[a]
                              for a in range(board_size)]
                h = heuristica(mock_board)
                row[j] = h

                if h < menor_valor:
                    menor_valor = h
                    options = [j if i == a else 'X' for a in range(board_size)]
                elif h == menor_valor:
                    options[i] = j
    print('\nopções:', options)
    return options


def get_indexes(options):
    return [idx for idx in range(board_size) if options[idx] != 'X']


print(board)
print('h(board):', heuristica(board), '\n')
options = calculate_neighbours(board)

for i in range(1, 1000):
    if (options.count('X') == board_size):
        print('Resultado encontrado em %i interações' % (i-1))
        break

    print('\nRODADA', i)

    indexes = get_indexes(options)

    if (len(indexes) > 1):
        ind = indexes[random.randint(0, len(indexes) - 1)]
    else:
        ind = indexes[0]

    board[ind] = options[ind]

    print(board)
    print('h(board):', heuristica(board), '\n')
    options = calculate_neighbours(board)

"""

Para o item (d), como deveria ser o calculo de avaliação

"""
