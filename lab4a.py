#!/usr/bin/env python3
# Strings 1

# Given strings
str1 = 'Hello World!!'
str2 = 'Seneca College'

# Given numbers
num1 = 1500
num2 = 1.50

# Function to get the first five characters of a string
def first_five(input_string):
    return input_string[:5]

# Function to get the last seven characters of a string
def last_seven(input_string):
    return input_string[-7:]

# Function to extract the middle number from a number
def middle_number(input_number):
    num_str = str(input_number)
    if len(num_str) >= 3:
        return num_str[1:3]  # Return second and third characters
    return num_str

# Function to get the first three characters of the first string and the last three characters of the second string
def first_three_last_three(str1, str2):
    return str1[:3] + str2[-3:]

# Function to join two sets
def join_sets(set1, set2):
    return set1 | set2  # Union of set1 and set2

# Function to match (intersect) two sets
def match_sets(set1, set2):
    return set1 & set2  # Intersection of set1 and set2

# Function to get the symmetric difference of two sets
def diff_sets(set1, set2):
    return set1 ^ set2  # Symmetric difference of set1 and set2

if __name__ == '__main__':
    print(first_five(str1))                 # Output: Hello
    print(first_five(str2))                 # Output: Senec
    print(last_seven(str1))                 # Output: World!!
    print(last_seven(str2))                 # Output: College
    print(middle_number(num1))              # Output: 50
    print(middle_number(num2))              # Output: .5
    print(first_three_last_three(str1, str2))  # Output: Helege
    print(first_three_last_three(str2, str1))  # Output: Send!!

