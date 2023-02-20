import graphics
import start


class Engine:
    """Engine of the game"""

    def __init__(self, len_word=(), word='', letter='', guess=[], control=set(), count=0, error=0, tries=7):
        # print('Игра началась!')
        self.len_word = len_word
        self.word = word
        self.letter = letter
        self.guess = guess
        self.control = control
        self.count = count
        self.error = error
        self.tries = tries

    # рандомайзер для подбора слова по выбранной сложности:
    def randomizer(self, len_word):
        from random import choice
        self.len_word = len_word
        print("Загадывается слово!")
        with open('Hangman.txt', 'r', encoding='utf-8') as text:
            text = text.read().split()
            while len(self.word) not in (list(range(self.len_word[0], self.len_word[1]+1))):
                self.word = choice(text)
        self.word = self.word.upper()
        # print(f'Слово загадано! {self.word}')
        print(f'Слово загадано!')
        self.guess = ['_'] * len(self.word)
        print(*self.guess)

    # алгоритм угадывания слова
    def target(self, letter):
        self.letter = letter
        if self.letter in self.control or self.tries == 0 or self.letter not in self.word:
            print(f'Нет такой буквы ({self.letter}) в слове или она уже вводилась! Попробуйте ещё раз!')
            self.control.add(self.letter)
            self.count += 1
            self.error += 1
            self.tries -= 1
            print(f'Осталось {self.tries} попыток')  # For update: check ending!
            print(graphics.gallows(self.error))
            print(*self.guess)
            print()
            if self.tries == 0:
                print(f'Вы не смогли угадать загаданное слово: {self.word}. Игра окончена!')
                print()
                print(start.GuiGame.__str__())
                return False
        elif self.letter in self.word and self.letter not in self.control:
            print(f'Есть буква {self.letter} в слове')
            for i in range(len(self.word)):
                if self.letter == self.word[i]:
                    self.guess.pop(i)
                    self.guess.insert(i, self.letter)
                    self.control.add(self.letter)
                    self.count += 1
                    if '_' not in self.guess:
                        print(f'Поздравляем! Вы угадали слово {self.word} за {self.count} попыток(ки)!')
                        print(f'Вами сделано {self.error} ошибок(ки)')  # For update: check ending!
                        print()
                        print(start.GuiGame.__str__())
                        return False
            print(*self.guess)
        return True


a = Engine()

