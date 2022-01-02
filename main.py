"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name    : Ryan Finally
Date    : January 2nd, 2022
Place   : Pontianak, West Borneo, Indonesia

This is a simple program which will ask you to guess a number and 
give a hint for every wrong guesses that you made.

We start by defining the key concept of this program 
based on the description
-finish     : A condition when the game ended  
-ingame     : A condition when the player are given the rules
              and guessing the number chosen by the program
-start      : A condition when the program ask whether the player 
              wants to play or not
-intro      : A condition when the program welcome the player and
              ask his/her name

Let us get into the detail.
finish  : 
- victory message
- defeat message

ingame  :
- rules
- play

start   :
- proceed?

intro   :
- welcome message
- ask name

Each of this key concept will be made as class
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from random import randint
from sys import exit

class Finish:
    def victory_message(self, number, guess):
        self.number = number
        self.guess = guess
        print("That was awesome!!!\n")
        print(f"Your guess was {self.guess}.")
        print(f"The secret number was {self.number}.")
        exit()

    def defeat_message(self, number, guess):
        self.number = number
        self.guess = guess
        print("Too bad. You almost got it.\n")
        print(f"Your guess was {self.guess}.")
        print(f"The secret number was {self.number}.")
        print("\nTry again later!")
        exit()

finish = Finish()

class In_game:
    __chances = 5
    def rule(self):
        print("    \"RULE OF THE GAME\"\n  ")
        print("-You have 5 chances to guess.")
        print("-For every wrong guess, you ")
        print(" will be given a hint. ")
        print("-If you guess it right then")
        print(" it is a win. If not, then")
        print(" it is a lose.")
        print("-The game will end when you")
        print(" guess the number, or run out")
        print(" of chances.")

    def result(self, result):
        self.result = result
        return self.result

    def play(self):
        self.number = randint(1,10)
        try:
            while self.__chances !=0:
                self.guess = int(input("Guess a number: ")) 
                self.__chances -= 1
                if self.guess == self.number:
                    self.result(True)
                elif self.guess < self.number:
                    if self.number - self.guess >= 3:
                        print("Well, that's too small.")
                    else:
                        print("So close! Bigger!")  
                elif self.guess > self.number:
                    if self.guess - self.number >= 3:
                        print("Well, that's too big.")
                    else:
                        print("So close! Smaller!")
                else:
                    print("What was that? Well, we count that as a chance!")
                print(f"You still have {self.chance} chances.")
            self.result(False)
            exit()
        except KeyboardInterrupt:
            print("\nHmm, dont just give up like that!")
            print("Well, see you later!")
            exit()
        except ValueError:
            print("1-10 only!")
            self.play()

in_game = In_game()

class Start:
    def proceed():
        pass

class Intro:
    def welcome_message():
        pass

    def username():
        pass


def main():
    pass

if __name__ == "__main__":
    main()



