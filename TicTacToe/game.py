from board import Board
from player import Player
class Game:
    def __init__(self, player1, player2, size):
        self._player1 = player1
        self._player2 = player2
        self._currentPlayer = self._player1
        self.size = size
        self._board = Board(size)
    
    def play(self):
        isWinner = False
        while(not isWinner):
            hasEmpty = self._board.getEmptyCells()
            if (not hasEmpty):
                print ("It's a tie.")
                break
            #play with currentplayer
            self._board.printBoard()
            print(f"{self._currentPlayer.getName()}'s Turn.")

            gridinput = input("Enter a position(row,col):").split(',')
            inputRow, inputCol = int(gridinput[0]), int(gridinput[1])
            if (not self._board.checkValidCell(inputRow, inputCol)):
                print("invalid position.Try again.")
                continue
            else:
                self._board.addPiece(inputRow, inputCol, self._currentPlayer.getPiece())
                if self._board.isWinner(inputRow, inputCol, self._currentPlayer.getPiece()):
                    print(f"{self._currentPlayer.getName()} wins!!")
                    break
                else:
                    self.switchPlayer()

    def switchPlayer(self):
        #switch between the 2 current players
        self._currentPlayer = self._player2 if self._currentPlayer == self._player1 else self._player1
        

    
    
    

