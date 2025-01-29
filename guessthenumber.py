import random
print(r"""
  ________                              ___________.__              _______               ___.
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \\
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/
""")
num = random.randint(1,100)
chance = 5
guess = 1
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
diff = (input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
if diff == "easy":
    chance = 10
    print("You have 10 attempts remaining to guess the number.")
else:
    print("You have 5 attempts remaining to guess the number.")
while chance > 0:
    chance -= 1
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == num:
        print("Congrats! You guessed the number in " + str(chance) + " attempts.")
        break
    else:
        if guess > num:
            print("Your guess is too high.")
        elif guess < num:
            print("Your guess is too low.")

if chance == 0:
    print("Sorry, you lose to guess the number.")
