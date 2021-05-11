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

class ChessBoard:
    
    def __init__(self, size):
        self.size = size
        self.chess_board = []

    def generate_chess_board(self):
        size = self.size
        chess_board = [[0] * size for i in range(size)]
        for row in chess_board:
            position = random.randrange(0,size, 1)
            row[position] = 'Q'        
        self.chess_board = chess_board

    def show_board(self):
        board = self.chess_board
        for row in board:
            print(row)

    def number_of_attacks(self):
        board = self.chess_board
        board_size = self.size
        for i in range(board_size):
            for j in range(board_size):
                if(board[i][j] == 'Q'):
                    for m in range(board_size):
                        for n in range(board_size):
                            if(board[m][n] != 'Q'):
                                if(m == i or n == j or (abs(m-i) == abs(n-j))):
                                    board[m][n] += 1

if __name__ == "__ChessBoard__":
    ChessBoard()



chess = ChessBoard(4)
chess.generate_chess_board()
chess.number_of_attacks()
chess.show_board()

"""

Para o item (d), como deveria ser o calculo de avaliação

"""