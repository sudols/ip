#! /usr/bin/python3.10

num = input('enter a num: ')


def check_if_numeric():
    try:
        float(num)
        return 'yes'
    except ValueError:
        return False


if check_if_numeric() == 'yes':
    print('square of', num, 'is', float(num)**2)
    print('cube of', num, 'is', float(num)**3)
else:
    print('that\'s not a valid number')
