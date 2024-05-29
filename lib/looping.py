#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num = 10
    while (num > 0):
        print(num)
        num -= 1
        print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return [num ** 2 for num in int_list]
    

def fizzbuzz():
    # code goes here! print 1-100 m-3 = Fizz m-5 = Buzz m-3&5 = FizzBuzz
    for num in range(1, 101):
        if (num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)