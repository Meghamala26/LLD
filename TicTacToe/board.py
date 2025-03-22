class Board:
    def __init__(self,size):
        self.size = size
        self._board = [['_' for _ in range(size)]for _ in range(size)]
        self.moves = 0
    
    def addPiece(self,row,col, piece):
        #add piece to the grid cell
        self._board[row][col] = piece
        self.moves+=1

    
    def checkValidCell(self,row,col):
        #checks if the grid cell is valid and empty
        if row<self.size and row>=0 and  col<self.size and col>=0 and self._board[row][col] == '_':
            return True
        else:
            return False
        
    def getEmptyCells(self):
        #return true/false for empty cells
        return True if self.moves < (self.size**2) else False

    def printBoard(self):
        #print the whole board
        for row in range(self.size):
            print(', '.join(self._board[row]))
        print()

    def isWinner(self, row, col, piece):
        #check if currentplayer is winner
        #rule1: all cells in cur row has same piece
        rowWon, colWon, diagWon,antiDiagWon = True, True, True, True
        for c in range(self.size):
            if not self._board[row][c]== piece:
                rowWon=False
        #rule2: all cells in cur col has same piece
        for r in range(self.size):
            if not self._board[r][col] == piece:
                colWon=False
        #rule3: all cells in diagonal has same piece
        for i in range(self.size):
            if not self._board[i][i]==piece:
                diagWon = False
        #rule4: all cells in anti-diagonal has same piece
        for i in range(self.size-1, -1, -1):
            if not self._board[self.size-1-i][i]==piece:
                antiDiagWon=False
        return rowWon or colWon or diagWon or antiDiagWon

    


