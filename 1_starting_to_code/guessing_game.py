#!/bin/python3.4
# Description: Gaming exercise

print("Welcome!")

g = input("Guess the number: ")

guess = int(g)

if guess == 5:

  print("You win!")

else:

 if guess > 5:

    print("Too high!")

 else:

  if guess <= 5:

    print ("Too low!")

  else:

    print ("You lose!")

print("Game over!")
