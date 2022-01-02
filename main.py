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



class In_game(object):
    def __init__(self):
        print("    \"RULE OF THE GAME\"\n  ")
        print("-You have 5 chances to guess.")
        print("-For every wrong guess, you ")
        print(" will be given a hint. ")
        print("-If you guess it right then")
        print(" it is a win. If not, then")
        print(" it is a lose.")
        print("-The game will end when you")
        print(" guess the number, or run out")
        print(" of chances.\n")

    def play(self):
        self.chances = 5
        self.number = randint(1,10)
        try:
            while self.chances !=0:
                self.guess = int(input("Guess a number: "))
                # print(self.number)
                self.chances -= 1
                if self.guess == self.number:
                    return True
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
                print(f"You still have {self.chances} chances.")
            return False
            exit()
        except KeyboardInterrupt:
            print("\nHmm, dont just give up like that!")
            print("Well, see you later!")
            exit()
        except ValueError:
            print("1-10 only!")
            self.play()



class Start:
    def proceed(self, username):
        self.username = username
        print(f"Are you ready, {self.username}?")
        try:
            self.user_input = input("[Y/N] >")
            if self.user_input == 'Y' or self.user_input == 'y':
                print("\nNice! Be Ready!")
                return True
            elif self.user_input =='N' or self.user_input == 'n':
                print("Why are you even here?")
                exit()
            else:
                print("What was that?")
                raise ValueError
        except ValueError:
            print("\nPlease learn to type!")
            self.proceed()
        except KeyboardInterrupt:
            print("\nLater!")
            exit()



class Intro:
    def __init__(self):
        print("Welcome to Guessing Game!")

    def username(self):
        try:
            print("Please tell us your name!")
            self.username = input('>')
            return self.username
        except KeyboardInterrupt:
            print("\nBye")
            exit()
        except Exception as e:
            print(e)



def main():
    intro = Intro()
    finish = Finish()
    username = intro.username()
    start = Start()
    result = start.proceed(username)
    if result == True:
        in_game = In_game()
        final_result = in_game.play()
    
    if final_result == True:
        print("nice")
    else:
        print("Not nice")
    

if __name__ == "__main__":
    main()



