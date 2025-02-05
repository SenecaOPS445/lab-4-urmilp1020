#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(input_string):
    # Return the first five characters of the string
    return input_string[:5]

def last_seven(input_string):
    # Return the last seven characters of the string
    return input_string[-7:]

def middle_number(input_number):
    # Convert number to string, and return the second and third characters
    str_number = str(input_number)
    # Ensure the number has at least two digits
    return str_number[1:3] if len(str_number) > 2 else str_number[1]

def first_three_last_three(str1, str2):
    # Concatenate the first three characters of str1 and last three characters of str2
    return str1[:3] + str2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
