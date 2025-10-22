#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def input_function():
  user_input = None
  while (type(user_input) != int) or (user_input <= 0):
    try: 
      user_input = int(input("Please enter a positive integer for Fibonacci Sequence: "))
    except ValueError:
      print("Invalid input! Please enter a positive integer.")
  return user_input

def fibonacci(n):
  fib_sequence = []
  a = 0
  b = 1
  for i in range(n):
    fib_sequence.append(a)
    a, b = b, a + b
  return fib_sequence

def print_sequence(sequence):
  print("Your Fibonacci sequence:")
  for n in sequence:
    print(n)

user_input = input_function()
sequence = fibonacci(user_input)
print_sequence(sequence)
    
    
    
  
                        
  
