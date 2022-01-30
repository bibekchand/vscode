def even_odd(x):
    if (x % 2 == 0):
        return True
    else:
        return False


my_number=int(input('input a numer here'))
if even_odd(my_number):
    print('this is even')
else:
    print('this is odd')
