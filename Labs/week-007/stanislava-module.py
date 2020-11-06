from random import randint
class Game:

    def __init__(self):
        self.max_guesses = 4
        self.guesses = 0
        self.random_number = randint(1,15)
        
    @staticmethod
    def message():
        print("Let's Play, you have 4 tries to guess a number between 1 and 15")
        
    def start(self):
        Game.message()
        win = self.user_guesses()
        if win:
            print("You win")
        else:
            print("You lose")
            
    def user_guesses(self):
        while self.guesses < self.max_guesses:
            guess = input("Try to guess: ")
            if int(guess) == self.random_number:
                return True
            self.guesses += 1
        return False
    
if __name__ == '__main__':
    game = Game()
    game.start()

