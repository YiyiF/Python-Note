number = 23
running = True

while running:
    guess = int(input('Enter an integer:'))

    if guess == number:
        #新块从这里开始
        print('Congratulations, you guessed it.')
        #这将导致while循环中止
        running=False
    elif guess < number:
        print('No, it is a little higher than that')
    else:
        print('No, it is a little lower than that')
else:
    print('The while loop is over.')
print('Done')