import random

def getMaxRoll():
    while True:
        try:
            maxRoll = int(raw_input('Please enter your maximum roll:'))
        except ValueError:
            print('Your max roll needs to be a whole number.')
            continue
        else:
            break
    return maxRoll
def rollDice(maxRoll):
    print('Dice is rolling...')
    userRoll = str(random.randrange(1, maxRoll))
    print('Your result is: ' + userRoll)
    return
def askUserReroll():
    while True:
        userReroll = raw_input('Reroll? (Enter Y or N):')
        if userReroll not in ('Y', 'N', 'y', 'n'):
            print('Response must be Y or N')
        else:
            break
    if userReroll in "Y":
        askUserSameDice()
        askUserReroll()
    else:
        print('Thank you!')
        exit()
def askUserSameDice():
    while True:
        userSameDice = raw_input('Same dice? (Enter Y or N):')
        if userReroll not in ('Y', 'N', 'y', 'n'):
            print('Response must be Y or N')
        else:
            break
    if userSameDice in "Y":
        rollDice(maxRoll)
        return
    else:
        newMax = getMaxRoll()
        rollDice(newMax)
        return

print('Hello! This is Jock\'s Python Dice')
maxRoll = getMaxRoll()
userResult = rollDice(maxRoll)
askUserReroll()
