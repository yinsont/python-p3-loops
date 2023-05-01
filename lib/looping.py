#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i-= 1 
    print ('Happy New Year!')

def square_integers(int_list):
    # code goes here!
    squared = list()
    for int in int_list:
        square = int * int
        squared.append(square)
    return squared
    pass

def fizzbuzz():
    # code goes here!
    n = 1
    while n <= 100:
        if (n % 3 == 0 and n % 5 == 0):
          print('FizzBuzz')
        elif (n % 5 == 0):
          print('Buzz')
        elif (n % 3 == 0):
          print('Fizz')
        else: print(n)
        n += 1
    pass
