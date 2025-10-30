import random
computer =random.choice([-1,0,1])
youstr = input("Enter your choice (S for Snake, w for Water, g for Gun): ")
youDict = {"S": 1, "w": -1, "g": 0}
you = youDict[youstr]
reverseDict ={1:"Snake",-1:"Water",0:"Gun"}

you = youDict[youstr]

print(f" You choose {reverseDict[you]}\n Computer choose{reverseDict[computer]}")

if computer == you:
    print("It's a Draw!")

else:
    '''
    if computer == -1 and you == 1:(computer - you) = -2
        print("You Win!")

    elif computer == -1 and you == 0:(computer - you) = -1
        print("You Lose!")

    elif computer == 1 and you == -1:(computer - you) = 2
        print("You Lose!")

    elif computer == 1 and you == 0:(computer - you) = 1
        print("You Win!")

    elif computer == 0 and you == -1:(computer - you) = 1
        print("You Win!")

    elif computer == 0 and you == 1: (computer - you) = -1
        print("You Lose!")

    '''
    if((computer - you )== -1 or (computer - you)==2):
        print("You lose!")

   
    else:
        print("You win")
