
user_input = str(input("Choose 'r' for rock, 's' for scissor and 'p' for paper: ").lower())

import random

def main():
    computer = random.choice(['r','p','s'])
    print(computer)

    if user_input == computer[0]:
        print("It\'s a tie")

    else:
        if (user_input == 's' and computer[0] == 'p') or (user_input == 'r' and computer[0] == 's') or\
            (user_input == 'p' and computer[0] == 'r') :
            print("You won")

        else:
            print("You loss")

if __name__ == "__main__":
    main()
