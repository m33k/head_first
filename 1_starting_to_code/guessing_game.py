#!/bin/python3.4
# Description: Gaming exercise
# Version 4: Make game generate numbers and ask gamer for the number until they guess it correctly.

from random import randint
secret = randint(1,10)

guess = int(input("Guess the number: "))

while guess != secret:
 if guess < secret:
   print("Too Low!")
 if guess > secret:
   print("Too High!")

 guess = int(input("Guess the number: "))

if guess == secret:
  print("You got it!")
  print("Thanks for playing!")

