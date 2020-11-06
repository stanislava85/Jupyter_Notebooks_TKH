from random import randint
class GuessingGame:
    """
    max_guess = 3
    guesses = 0
    """
    def __init__(self):
        self.max_guesses = 3
        self.guesses = 0
        self.random_number = randint(1,3)
    @staticmethod
    def welcome_message():
        print("Welcome to guessing game")
    def start(self):
        GuessingGame.welcome_message()
        win = self.handle_guesses()
        if win:
            print("You have won")
        else:
            print("You have lost")
    def handle_guesses(self):
        while self.guesses < self.max_guesses:
            guess = input("Enter a guess ")
            if int(guess) == self.random_number:
                return True
            self.guesses += 1
        return False
if __name__ == '__main__':
    game = GuessingGame()
    game.start()