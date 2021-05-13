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
import math
import copy


"""
Define o tamanho do tabuleiro
"""
board_size = 4


"""
Define a posição das rainhas em um tabuleiro,
onde o índice é a coluna do tabuleiro e o
valor é a linha em que a rainha está posicionada
"""


def generate_board(board_size):
    return [random.randint(0, board_size - 1) for i in range(board_size)]


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
Método utilitário para calcular os vizinhos 
com a menor heurísticas para mover as rainhas 
pelo tabuleiro
"""


def first_neighbour(board):
    neighbour = copy.deepcopy(board)
    h_atual = heuristica(board)  # heurística do quadro atual
    for i in range(board_size):  # iteração por todas as linhas
        for j in range(board_size):  # iteração por todas as colunas
            if (j != board[i]):  # Se não for a posição de uma rainha
                mock_board = [j if a == i else board[a]
                              for a in range(board_size)]
                h = heuristica(mock_board)  # Verifica a heurística do vizinho
                if h < h_atual:  # se for uma nova menor heurística possível
                    neighbour[i] = j
                    break
    return neighbour


"""
Método utilitário para calcular os vizinhos 
com a menor heurísticas para mover as rainhas 
pelo tabuleiro
"""


def calculate_neighbours(board):
    # lista de vizinhos com heurística menor ou igual
    neighbours = ['X' for a in range(board_size)]
    h_atual = heuristica(board)  # heurística do quadro atual
    menor_valor = h_atual  # inicialização do comparador de menor heurística dos vizinhos

    for i in range(board_size):  # iteração por todas as linhas
        #row = [0 for i in range(board_size)]

        for j in range(board_size):  # iteração por todas as colunas

            # if(j == board[i]):
            #row[j] = 'Q'
            # else:
            if (j != board[i]):  # Se não for a posição de uma rainha
                mock_board = [j if a == i else board[a]
                              for a in range(board_size)]
                h = heuristica(mock_board)  # Verifica a heurística do vizinho
                #row[j] = h
                if h < menor_valor:  # se for uma nova menor heurística possível
                    menor_valor = h  # atualiza a menor heurística possível
                    neighbours = [j if i == a else 'X' for a in range(
                        board_size)]  # reinicia a lista de vizinhos
                elif h == menor_valor:  # se for mais um possível vizinho na mesma heurística
                    neighbours[i] = j  # adiciona a lista

    return neighbours


"""
Método utilitário para exibir a configuração
atual do tabuleiro
"""


def show_board(board):
    for i in range(board_size):  # iteração por todas as linhas
        row = [0 for i in range(board_size)]
        for j in range(board_size):  # iteração por todas as colunas
            if(j == board[i]):
                row[j] = 'Q'
            else:
                mock_board = [j if a == i else board[a]
                              for a in range(board_size)]
                # Verifica a heurística do vizinho
                row[j] = heuristica(mock_board)
        print(row)


"""
Método para recuperar as indíces dos possíveis ivizinhos
"""


def get_indexes(neighbours):
    return [idx for idx in range(board_size) if neighbours[idx] != 'X']


"""
Método execução do hill climbing
"""


def simple_hill_climbing(init_board):
    print('\nHill Climbing\n')
    # inicializa o tabuleiro com a configuração inicial
    board = copy.deepcopy(init_board)
    count = 0
    while True:

        print('\nRODADA', count)
        print(board)
        print('h(board):', heuristica(board))  # exibe heurística atual

        count += 1
        neighbour = first_neighbour(board)  # busca o primeiro vizinho
        board = neighbour  # atribui vizinho para a rodada atual

        if (heuristica(board) == 0):  # encerra se alcançar o objetivo
            print('\nResultado encontrado em %i interações \n' % (count))
            show_board(board)
            break


"""
Método execução do hill climbing
"""


def hill_climbing(init_board):
    print('\nHill Climbing\n')
    # inicializa o tabuleiro com a configuração inicial
    board = copy.deepcopy(init_board)
    count = 0
    while True:
        print(board)
        print('h(board):', heuristica(board))  # exibe heurística atual
        neighbours = calculate_neighbours(board)  # busca os possíveis vizinhos
        count += 1

        if (neighbours.count('X') == board_size):  # encerra se não houverem vizinhos possíveis
            print('\nResultado encontrado em %i interações \n' % (count-1))
            show_board(board)
            break

        print('\nRODADA', count)

        # retorn os índices das linhas em que a rainha pode ser movida
        indexes = get_indexes(neighbours)

        if (len(indexes) > 1):  # havendo mais de uma possibilidade
            # escolhe-se de forma aleatória a linha a ser modificada
            ind = indexes[random.randint(0, len(indexes) - 1)]
        else:  # caso contrário, escolhe-se a única opção
            ind = indexes[0]

        # atualização da posição das rainhas no quadro para a próxima rodada
        board[ind] = neighbours[ind]


"""
Método de geração de um vizinho aleatório
sem que seja salvo um mapa dos possíveis vizinhos
"""


def random_neighbour(board):
    # atribui o tabuleiro atual para o vizinho
    neighbour = copy.deepcopy(board)
    while True:  # gera valores aleatórios para a nova posição da rainha
        row = random.randint(0, board_size - 1)
        column = random.randint(0, board_size - 1)
        if (board[row] != column):  # se não houver uma rainha na posíção
            neighbour[row] = column  # atribui a nova posição á rainha da fila
            break
    return neighbour  # retorna o vizinho


"""
Método execução do simulated annealing
"""


def simulated_annealing(init_board, max_iter, temp, alpha):
    print('\nSimultaed Annealing\n')
    board = copy.deepcopy(init_board)  # inicializa o board
    best_board = copy.deepcopy(init_board)  # inicializa o best_board
    currTemp = temp  # inicializa o tempo

    for i in range(max_iter):
        print('\n', best_board)
        print('h(board):', heuristica(best_board))

        if (heuristica(best_board) == 0):
            print('\nResultado encontrado em %i interações \n' % (i))
            break

        print('\nRODADA', i+1)

        vizinho = random_neighbour(board)  # gera um vizinho aleatório
        delta = heuristica(vizinho) - heuristica(board)  # calcula o delta

        if (delta <= 0):  # se o delta for menor ou igual a zero
            board = vizinho  # atribui o vizinho gerado para o board atual
            # se a heurística for menor no vizinho que no best_board
            if (heuristica(vizinho) <= heuristica(best_board)):
                best_board = vizinho  # atribui o vizinho gerado para o best_board
        else:
            # calcula a probabilidade de ser aceito como próximo estado a ser considerado
            if (math.exp(-delta/currTemp) > random.random()):
                board = vizinho  # atribui o vizinho gerado para o board atual

        currTemp = alpha*currTemp  # atualiza o tempo corrente

    final_h = heuristica(best_board)
    print(best_board, final_h, '\n')
    show_board(best_board)  # resultado final
    return (best_board, final_h)


"""
Inicializa o programa
"""
for i in range(2, 6):
    board_size = 2**i
    for j in range(5):
        board = generate_board(board_size)
        simple_hill_climbing(board)
        hill_climbing(board)
        simulated_annealing(board, 100, 0.7, 0.25)
