#!/usr/bin/env python3
def getting_positive_number():

  while True:
    user_input = input("Enter Number of Fibonacci Terms: ")
    if user_input.isdigit() and int(user_input) > 0:
        return int(user_input)
    else:
      print("Invalid, Try again")

def fibonacci_calculator(n):

  sequence = []
  a, b = 0, 1
  for _ in range(n):
    sequence.append(a)
    a, b = b, a + b
  return sequence

def fibonacci(sequence):
  print("Fibonacci sequence: ")
  print(", ".join(str(num) for num in sequence))


def main():
  n_terms = getting_positive_number()
  fibonacci_sequence = fibonacci_calculator(n_terms)
  fibonacci(fibonacci_sequence)

main()
# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
