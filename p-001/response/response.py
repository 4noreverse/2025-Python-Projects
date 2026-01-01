from validator_collection import validators, checkers
x = input('What\'s your email address?')
y = checkers.is_email(x)
if y == True:
    print('Valid')
if y == False:
    print('Invalid')
