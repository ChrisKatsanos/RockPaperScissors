import time
import random
#choice = random.randint(1 ,3)
#1 = "rock"
#2 = "paper"
#3 = "scissors"
counter = 2
score1 = 0
score2 = 0
player1 = input(" What is your name player1?")
player2 = input(" What is your name player2?")
while counter > 0 :

    choice1 = random.randint(1,3)
    choice2 = input(" What is your choice player 2?")

    if choice1 == 1 and choice2 == "scissors":
        print("player 1 is thinking!!!")
        score1 += 1
        time.sleep (2)
        print ("player 1 chose: rock, player 2 chose: scissors")
        time.sleep (2)
        print(player1, "you win!", score1 , score2)
        time.sleep(2)
    elif choice1 == 3 and choice2 == "rock":
        print("player 1 is thinking!!!")
        score2 += 1
        time.sleep (2)
        print("player 1 chose: scissors, player 2 chose: rock")
        time.sleep (2)
        print(player2, "you win!", score1 , score2)
        time.sleep(2)
    elif choice1 == 2 and choice2 == "rock":
        print("player 1 is thinking!!!")
        score1 += 1
        time.sleep (2)
        print("player 1 chose: paper, player 2 chose: rock")
        time.sleep (2)
        print(player1, "you win!", score1 , score2)
        time.sleep(2)
    elif choice1 == 1 and choice2 == "paper":
        print("player 1 is thinking!!!")
        score2 += 1
        time.sleep (2)
        print("player 1 chose: rock, player 2 chose: paper")
        time.sleep (2)
        print(player2, "you win!" ,score1, score2)
        time.sleep(2)
    elif choice1 == 2 and choice2 == "scissors":
        print("player 1 is thinking!!!")
        score2 += 1
        time.sleep (2)
        print("player 1 chose: paper, player 2 chose: scissors")
        time.sleep (2)
        print(player2, "you win!", score1 ,score2)
        time.sleep(2)
    elif choice1 == 3 and choice2 == "paper":
        print("player 1 is thinking!!!")
        score1 += 1
        time.sleep (2)
        print("player 1 chose: scissors, player 2 chose: paper")
        time.sleep (2)
        print(player1, "you win!",score1 , score2)
        time.sleep(2)
    elif choice1 == 1 and choice2 == "rock":
        print("player 1 is thinking!!!")
        time.sleep(2)
        print ("player 1 and player 2 chose: rock")
        time.sleep (2)
        print("its a tie!", score1 , score2)
        time.sleep(2)
    elif choice1 == 2 and choice2 == "paper":
        print("player 1 is thinking!!!")
        time.sleep(2)
        print ("player 1 and player 2 chose: paper")
        time.sleep (2)
        print("its a tie!", score1 , score2)
        time.sleep(2)
    elif choice1 == 3 and choice2 == "scissors":
        print("player 1 is thinking!!!")
        time.sleep(2)
        print("player 1 and player 2 chose: scissors")
        time.sleep (2)
        print("its a tie!", score1 , score2)
        time.sleep(2)
    else:
        print("type rock, paper or scissors")
    counter = counter - 1

print("Final score,", "player 1:" ,score1,"player 2:", score2, "!")


