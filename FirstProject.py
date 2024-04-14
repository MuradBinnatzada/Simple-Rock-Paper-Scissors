import random
print("This is a simple 'rock paper scissors' game.")
print("Let's start!")
gametype = int(input("You want to play regular or best of 3? '1' for regular, '2' for best of 3: "))


def user():
    userturn = input("Enter your choise rock/paper/scissors: ").lower()
    while userturn not in ['rock', 'paper', 'scissors']:
        print("Invalid choise!")
        userturn = input("Enter your choise rock/paper/scissors: ").lower()
    return userturn


def computer():
    computerturn = random.choice(["rock", "paper", "scissors"])
    return computerturn


def getwinner(userturn, computerturn):
    global winner
    winner = None
    if (userturn == 'rock' and computerturn == 'scissors') or \
       (userturn == 'scissors' and computerturn == 'paper') or \
       (userturn == 'paper' and computerturn == 'rock'):
        print("You won!")
        winner = "user"
    elif userturn == computerturn:
        print("Nice try, it's a tie!")
    else:
        print("You lost!")
        winner = "computer"


def getgametype():
    if gametype == 1:
        startgame()

    elif gametype == 2:
        userwincount = 0
        pcwincount = 0
        while userwincount <= 2 or pcwincount <= 2:
            startgame()
            if winner == "user":
                userwincount += 1
            elif winner == "computer":
                pcwincount += 1
        else:
            if userwincount == 3:
                print(f"You won! It's {userwincount} - {pcwincount}.")
            elif pcwincount == 3:
                print(f"You lost! It's {userwincount} - {pcwincount}.")


def startgame():
    userturn = user()
    computerturn = computer()
    print(f"Your choise is {userturn}")
    print(f"Computer choise is {computerturn}")

    winner(userturn, computerturn)


getgametype()
