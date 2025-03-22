from player import Player
from game import Game
class TicTacToeMain:
    @staticmethod
    def run():
        player1 = Player('player1', 'X')
        player2 = Player('player2', 'O')
        game = Game(player1, player2, 3)
        game.play()

if __name__ == "__main__":
    TicTacToeMain.run()