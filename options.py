

class Options:
    """Options of the game"""

    def __init__(self, diff='', open_let=0):
        # print('option init')
        self.diff = diff
        self.open_let = open_let

    def game_difficulty(self, diff):
        self.diff = diff
        # word length is limited to 6 characters
        if self.diff == 'лёгкая':
            # print('easy')
            return 1, 6
        # word length is limited from 7 to 9 characters
        if self.diff == 'средняя':
            # print('middle')
            return 7, 9
        # word length 10 or more characters
        if self.diff == 'сложная':
            # print('hard')
            return 10, 20

    # signal for open letters in guessed word
    def open_let(self):
        if self.open_let == 1:
            pass


res = Options()
# print(res)
# print(res.game_difficulty())
