def fool(x):
    if (x % 2 == 0):
        return True
    else:
        return False


number = int(input('input a number:'))
if fool(number):
    print('this is even')
else:
    print('this is odd')
