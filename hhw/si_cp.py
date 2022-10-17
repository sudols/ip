#! /usr/bin/python3.10

principal = input('principal amount: ')
rate_of_interest = input('rate of interest: ')
time = input('time in years: ')


def check_if_numeric():
    try:
        int(principal)
        int(time)
        float(rate_of_interest)
    except ValueError:
        return False


if check_if_numeric() == False:
    print('input correct value')
else:
    int(principal)
    int(time)
    float(rate_of_interest)


si = principal*rate_of_interest*time/100
ci = principal*((1+rate_of_interest)/100)

diff = ci - si

print('simple interest', si)
print('compound interest', ci)
print('difference between simple interest and compound interest is: ', diff)
