# Tic Tac Toe Board
class Board:
    # Creates a 3x3 grid for the board
    def __init__(self):
        dim = 3
        self.grid = []
        for c in range(0,dim): self.grid.append([' ' for i in range(dim)])

    # place a players marker inside a cell in the grid
    # args(string of players marker, int row, int cell)
    # return(none)
    def place_marker(self, marker, row, cell):
        self.grid[row][cell] = marker
        return self.grid

    # prints the board
    # args(none)
    # returns(none)
    def display(self):
        print('')
        for r in range(0, len(self.grid)):
            print(*self.grid[r], sep='|')
            if r != 2: print('- - -')
        print('')

 
# player object
class Player:
    # creates  the player object
    # args(string of the players marker, int players number)
    # returns(none)
    def __init__(self, marker, num):
        self.marker = marker
        self.num = num

    # says the player has won
    # args(none)
    # returns(True)
    def has_won(self):
        print('Player #%s Won!!' %(self.num))
        return True

    # checks if the player has won
    # args(board object)
    # returns(True or False)
    def check_won(self, board):
        if board.grid[0][0] == self.marker and board.grid[1][1] == self.marker and board.grid[2][2] == self.marker: return self.has_won() # checks for left diagonal win
        if board.grid[0][2] == self.marker and board.grid[1][1] == self.marker and board.grid[2][0] == self.marker: return self.has_won() # checks for right diagonal win
        for i in range(len(board.grid)): # checks for a horizontal/vertical win
            if(board.grid[0][i] == self.marker and board.grid[1][i] == self.marker and board.grid[2][i] == self.marker) or (board.grid[i][0] == self.marker and board.grid[i][1] == self.marker and board.grid[i][2] == self.marker): return self.has_won()
        return False
    
    # lets the player select a square to place their marker
    # args(board object the player is playing on)
    # returns(none)
    def turn(self, board):
        print("Player #%s's Turn:" %(self.num))
        played = False
        while not played: 
            row = int(input('Row[1-3]: '))-1
            cell = int(input('Cell[1-3]: '))-1
            try:
                if board.grid[row][cell] == ' ' and 0 <= row <= 2 and 0 <= cell <= 2: played = True
                else: print('Invalid Input...')
            except: print('Invalid Input...')
        board.grid = board.place_marker(self.marker, row, cell)
        board.display()
        won = self.check_won(board)
        return won
                    

# game object
class Game:
    # plays the game
    # args(none)
    # returns(none)
    def play(self):
        # initializes variables and objects
        board = Board()
        player1 = Player('O', '1')
        player2 = Player('X', '2')
        # while the game hasnt been one: player1 and player2 take turns
        while True:
            if player1.turn(board): break
            if player2.turn(board): break
            

# creates and plays the game
game = Game()
game.play()
