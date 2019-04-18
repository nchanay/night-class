""""
Tic-Tac-Toe
"""
from random import shuffle


class Player:
    """
    The player class has the player's actions
    """
    def __init__(self, player_name, token):
        self.name = player_name
        self.token = token

    def __repr__(self):
        return f'{self.name}'


class Game:
    """
    The game parameters
    """
    def __init__(self):
        self.board = [['1', '2', '3'],
                      ['4', '5', '6'],
                      ['7', '8', '9']]
        self.playerX = Player('Player X', 'X')
        self.playerO = Player('Player O', 'O')
        self.players = [self.playerX, self.playerO]

    def __repr__(self):
        board = '\n'
        count = 2
        for row in self.board:
            board += '\t' + ' | '.join(row) + '\n'
            if count > 0:
                board += '\t' + "---------" + '\n'
                count -= 1
        return board

    def move(self, num, player):
        space_dict = {1: self.board[0][0],
                      2: self.board[0][1],
                      3: self.board[0][2],
                      4: self.board[1][0],
                      5: self.board[1][1],
                      6: self.board[1][2],
                      7: self.board[2][0],
                      8: self.board[2][1],
                      9: self.board[2][2]}
        if space_dict[num] == str(num):
            space_dict[num] = player.token
            print(space_dict)
        else:
            print("oh no")
        # if self.board[num] == num:
        #     self.board[num] = player.token

    def calc_winner(self):
        winning_combo = ((0, 1, 2),
                         (3, 4, 5),
                         (6, 7, 8),
                         (0, 3, 6),
                         (1, 4, 7),
                         (2, 5, 8),
                         (0, 4, 8),
                         (2, 4, 6))

        for combo in winning_combo:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                winner = self.board[combo[0]]
                return f'{winner} is the winner!'
            else:
                return None

    def is_full(self):
        count = 0
        for i in self.board:
            if i == 'X' or i == 'O':
                count += 1
        if count == 9:
            return 'Full'
        else:
            return None

    def is_game_over(self):
        if self.calc_winner() is not None and self.is_full() is not None:
            return 'Game Over'

    def play(self):
        shuffle(self.players)
        loop = True
        while loop:
            for player in self.players:
                loop2 = True
                while loop2:
                    print(f"It is {player}'s turn")
                    num = input("Where would you like to place your token?\n> ")
                    if num.isdigit():# and num in range(0, 9):
                        num = int(num)
                        self.move(num, player)
                        print(self)
                        loop2 = False
                    else:
                        print("Please select a number from the board.")


def main():
    loop = True
    while loop:
        game = Game()
        print(game)
        game.play()
        while True:
            play_again = input('Do you want to play again? \n>').strip().lower()
            if play_again in ['y', 'yes', 'n', 'no']:
                break

        if play_again.startswith('n'):
            loop = False


if __name__ == '__main__':
    main()
