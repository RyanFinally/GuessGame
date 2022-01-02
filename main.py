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

class Intro:
    def __init__(self):
        print("Welcome to Guessing Game!\n")
        self.username()

    def username(self):
        try:
            print("Please tell us your name!")
            self.username = input('> ')
            print("\n")
            #return self.username
        except KeyboardInterrupt:
            print("\nBye")
            exit()
        except Exception as e:
            print(e)

class Start(Intro):
    def proceed(self):
        try:
            print(f"Are you ready, {self.username}?")
            self.user_input = input("[Y/N]> ")
            if self.user_input == 'Y' or self.user_input == 'y':
                print("\nNice! Be Ready!\n")
                return True
            elif self.user_input =='N' or self.user_input == 'n':
                print("Why are you even here?")
                exit()
            else:
                print("\nWhat was that?")
                raise ValueError
        except KeyboardInterrupt:
            print("\nLater!")
            exit()
        except ValueError:
            print("\nPlease learn to type!")
            self.proceed()
            

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

class In_game(Finish):
    def __init__(self):
        print("\n\"RULE OF THE GAME\"\n")
        print("-You have 5 chances to guess.")
        print("-For every wrong guess, you will be given a hint.")
        print("-If you guess it right then it is a win. If not, ")
        print(" then it is a lose.")
        print("-The game will end when you guess the number, ")
        print(" or run out of chances.\n")
         
        self.chances = 5
        self.number = randint(1,10)
        self.play()

    def play(self):
        try:
            while self.chances !=0:
                self.guess = int(input("Guess a number: "))
                # print(self.number)
                self.chances -= 1
                if self.guess == self.number:
                    self.victory_message(self.number, self.guess)
                elif self.guess < self.number:
                    if self.number - self.guess >= 3:
                        print("\nWell, that's too small.")
                    else:
                        print("So close! Bigger!")  
                elif self.guess > self.number:
                    if self.guess - self.number >= 3:
                        print("\nWell, that's too big.")
                    else:
                        print("So close! Smaller!")
                else:
                    print("What was that? Well, we count that as a chance!")
                print(f"You still have {self.chances} chances.\n")
            self.defeat_message(self.number, self.guess)
            exit()
        except KeyboardInterrupt:
            print("\nHmm, dont just give up like that!")
            print("Well, see you later!")
            exit()
        except ValueError:
            print("1-10 only! Well, we count that as a chance!")
            self.chances -= 1
            print(f"You still have {self.chances} chances.\n")
            self.play()


def main():
    # intro = Intro()
    try:
        start = Start()
        tmp = start.proceed()

        if tmp == True:
            finish = In_game()
    except KeyboardInterrupt:
        print("See you later!!")
    except Exception as e:
        print(e)
    finally :
        print("\n\nCreated By Ryan Finally")

if __name__ == "__main__":
    main()



