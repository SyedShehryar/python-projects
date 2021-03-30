import random

def guess(x):
    random_number = random.randint(1 , x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 & {x} : "))
        if guess < random_number :
            print ("Sorry , guess again. Too Low")

        elif guess > random_number :
            print ("Sorry , guess again. Too High")

    print (f"Yayy! You have guessed the number {random_number}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' :
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could also be high because high = low
        feedback = input(f"Is {guess} too high (h) , too low (l) , or correct (c) :")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay! The computer has guessed your number {guess}, correctly! ")

computer_guess(1000)  
