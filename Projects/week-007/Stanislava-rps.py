import random

class RPS:
    def __init__(self, rounds=3):
        self.rounds = rounds
        
    @staticmethod
    def welcome_message():
        print("Let's play Rock, Paper, Scissors!")
        
    def computers_turn(self):
        choices = {
            0: 'rock',
            1: 'paper',
            2: 'scissor'
        }
        turn = random.randint(0,2)
        return (turn, choices[turn])
    
    def your_turn(self, choice):
        if choice not in ['R', 'P', 'S']:
            raise ValueError("You must select one of ['R', 'P', 'S']")

        choices = {
            'R': (0, 'rock'),
            'P': (1, 'paper'),
            'S': (2, 'scissors'),
        }    
        return choices[choice] 
        
    def compare_turns(self,user_choice, computer_choice):
        game_results = {
            0: 'Draw!',
            1: 'You win!',
            2: 'Computer wins!'
        }
        key = (user_choice[0] - computer_choice[0]) % 3
        return game_results[key]
                
    def won_round(self):
        user_input = input("Please, select Rock (R), Paper (P), or Scissors (S).")
        computer_choice = self.computers_turn()
        print(f"Computer's choice is: {computer_choice}")
        user_choice = self.your_turn(user_input)
        print(f"your choice is: {user_choice}'")
        return self.compare_turns(user_choice, computer_choice)
        
    def run(self):
        RPS.welcome_message()
        print('Staring the game:')
        count = int(self.rounds)
        while count > 0:
            win = self.won_round()
            print(win)
            count -=1
            print(f"There is {count} round(s) left.")
            print("\n")


if __name__ == '__main__':
    rps = RPS()
    rps.run()