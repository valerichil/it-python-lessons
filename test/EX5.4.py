import random
while(True):
    level = int(input("Level: "))
    if level > 0:
        break
    else:
        continue


Answer = random.randint(1,level)

while(True):
    try:
        Guess = int(input("Guess: "))
        if Guess > 0:
            if Guess == Answer:
                print("Just right!")
                break
            elif Guess < Answer:
                print("Too Small!")
            else:
                print("Too large!")
    except ValueError:
        continue
