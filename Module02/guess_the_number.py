print('----------------------------------------')
print('           GUESS THE NUMBER APP         ')
print('----------------------------------------')

right_number = 71
guess = input('Guess a number between 0 and 100')

guess = float(guess)

if guess <= right_number:
    print('Sorry but') + guess + ('is lower than the number!')
elif guess >= right_number:
    print('Sorry but') + guess + ('is higher than the number!')
elif guess == right_number:
    print('YES! You got it. The number was') + right_number