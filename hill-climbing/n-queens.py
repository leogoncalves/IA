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
board_size = 4


"""

Define a posição das rainhas em um tabuleiro, 
onde o índice é a coluna do tabuleiro e o 
valor é a linha em que a rainha está posicionada

"""
def generate_board(board_size):
    return [random.randint(0, board_size - 1) for i in range(board_size)]

# board = generate_board(board_size)
board = [1,2,3,2]

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

Método utilitário para ver o tabuleiro

"""

def show_board(board):
    display = [0 for a in range(board_size)]
    for i in range(board_size):
        row = [0 for i in range(board_size)]
        menor_valor = 99999
        for j in range(board_size):
            if(j == board[i]):
                row[j] = 'Q'
            else:
                mock_board = [j if a == i else board[a] for a in range(board_size)]
                row[j] = heuristica(mock_board)
                if row[j] < menor_valor:
                    menor_valor = row[j]
                    display[i] = j
        print(row)
    print(display)

print(board)
print(heuristica(board))
show_board(board)







# class ChessBoard:
    
#     def __init__(self, size):
#         self.size = size
#         self.chess_board = []

#     def generate_chess_board(self):
#         size = self.size
#         chess_board = [[0] * size for i in range(size)]
#         for row in chess_board:
#             position = random.randrange(0,size, 1)
#             row[position] = 'Q'        
#         self.chess_board = chess_board

#     def show_board(self):
#         board = self.chess_board
#         for row in board:
#             print(row)

#     def number_of_attacks(self):
#         board = self.chess_board 
#         board_size = self.size
#         custo = 0
#         for row in range(board_size):
#             for column in range(board_size):
#                 if(board[row][column] == 'Q'):
#                     custo += self.calculator(board, row, column, row+1)
#                 else:
#                     board[row][column] = self.calculator(board, row, column, 0)
#         print(custo)
#         return custo
    
#     def calculator(self, board, row, column, init_row = 0):
#         board_size = self.size
#         custo = 0
#         for row2 in range(init_row, board_size):
#             for column2 in range(board_size):
#                 if(board[row2][column2] == 'Q'):
#                     if ((column == column2) or (abs(column2 - column) == abs(row2 - row))):
#                         custo += 1
#         return custo

# if __name__ == "__ChessBoard__":
#     ChessBoard()



# chess = ChessBoard(4)
# chess.generate_chess_board()
# chess.number_of_attacks()
# chess.show_board()

"""

Para o item (d), como deveria ser o calculo de avaliação

"""