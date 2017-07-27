#!/bin/python3.4
# Description: Gaming exercise
# Version 3: Make game ask gamer for the number until they guess it correctly.

answer = 5

guess = int(input("Guess the number: "))


while guess != 5:
 if guess < 5:
   print("Too Low!")
 if guess > 5:
   print("Too High!")
 guess = int(input("Guess the number: "))

