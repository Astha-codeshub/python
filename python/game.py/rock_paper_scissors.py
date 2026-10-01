import random
choices=['rock','paper','scissors']
computer=random.choice(choices)
you=input("Enter your choice:").strip().lower()
if computer=='rock' and you=='paper':
    print("you won")
elif computer=='rock' and you=='scissors':
    print("computer won")
elif computer=='paper' and you=='rock':
    print("computer won")
elif computer=='paper' and you=='scissors':
    print("you won")
elif computer=='scissors' and you=='rock':
    print("you won")
elif computer=='scissors' and you=='paper':
    print("computer won")
elif computer==you:
    print("Draw")
else:
    print("you entered the wrong choice.")
print("computer choose:",computer)
print("you entered:",you)
