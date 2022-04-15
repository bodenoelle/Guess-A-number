import random

exact_num = random.randint(1,100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses = [0]

while True:
    guess = int(input("Think of a number between 1 and 100.\n Enter your guess: "))

    if guess < 1 or guess > 100:
        print('WRONG ENTRY! Please input number between 1-100')
        continue
    if guess == exact_num:
        print(f'WELDONE! You guessed right in {len(guesses)} guesses!')
        break
    guesses.append(guess)
    if guesses[-2]:
        if abs(exact_num-guess) < abs(exact_num-guesses[-2]):
            print('CLOSER!')
        else:
            print('FARTHER!')
    else:
        if abs(exact_num-guess) <= 10:
            print('CLOSE!')
        else:
            print('FAR!')