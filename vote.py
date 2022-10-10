#! /usr/bin/python3.10

name = input('your name: ')
age = input('age: ')


def check_if_numeric_and_vote_eligible():
    try:
        if float(age) > 18:
            return 'Yes'
    except ValueError:
        return False


if check_if_numeric_and_vote_eligible() == False:
    print('input a valid age')
elif check_if_numeric_and_vote_eligible() == 'Yes':
    print('you\'re eligible for vote')
else:
    print('not eligible for vote :(')
