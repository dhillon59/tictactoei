class Tictac:
    def __init__(self):
        self.board = ['' for _ in range(9)]
        self.current_winner = None

    def printBoard(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('| '+ ' | '.join(row)+ ' |')

    @staticmethod
    def printNumberboard():
            numberboard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
            for row in numberboard:
                 print('| '+ ' | '.join(row)+ ' |')
                 
    def availablemoves(self):
         return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
         return ' ' in self.board
    
    def num_empty_squares(self):
         return self.board.count(' ')
    
    def make_move(self, square, letter):
         if self.board[square] == ' ':
              self.board[square] = letter

def play(game, x_player, o_player, print_game=True):
     if print_game:
          game.printNumberboard()
     while game.empty_squares():
          if letter == 'O':
               
          
