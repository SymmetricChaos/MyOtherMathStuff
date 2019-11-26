from time import sleep
from random import randint

def the_100_game():
    
    total = 0
    print("Starting at 0")
    print("You must add a number from 1 to 10 each time")
    print("Whoever brings the total to 100 wins!\n")
    while True:
        
        sleep(.5)
        player_move = int(input("Your Move:"))
        if player_move > 10 or player_move < 0:
            print("CHEATER! DISQUALIFIED! NIM WINS!")
            return 0
        else:
            total += player_move
        
        print(f"Total is now {total}")
        if total == 100:
            print("\nYou win!")
            return 1
        if total > 100:
            print("\nToo high, you lose.")
            return 0
        
        
        
        nim_move = 12-(total % 11)
        if nim_move == 11:
            nim_move = randint(1,10)
        if nim_move == 12:
            nim_move = 1
        
        print("\nNim is thinking.")
        sleep(1)
        print(f"Nim chooses {nim_move}")
        
        total += nim_move
        

        
        print(f"Total is now {total}")
        if total == 100:
            print("\nNim wins!")
            return 0
        
        
if __name__ == '__main__':
    the_100_game()