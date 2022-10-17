#! /usr/bin/python3.10

name = str(input('enter your name: '))


subject_1_marks = input('marks for subject 1: ')
subject_2_marks = input('marks for subject 2: ')
subject_3_marks = input('marks for subject 3: ')


def check_if_numeric():
    try:
        float(subject_1_marks)
        float(subject_2_marks)
        float(subject_3_marks)
    except ValueError:
        return False


if check_if_numeric() == False:
    print('marks is not valid, input a number.')
else:
    percentage_subject_1 = float(subject_1_marks)/100*100
    percentage_subject_2 = float(subject_2_marks)/100*100
    percentage_subject_3 = float(subject_3_marks)/100*100
    print()
    print('--------------\n')
    print('marks of', name, 'are:')
    print(
        ' subject 1:', percentage_subject_1,
        '\n subject 2:', percentage_subject_2,
        '\n subject 3:', percentage_subject_3
    )
