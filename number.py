import random
number = random.randint(1,100)
guess = 0
while guess != number:
  guess = int(input("Enter Guess: "))
  if (guess < number):
    print(" You need to Guess higher!")
  elif (guess > number):
    print("You need to Guess lower!")
  else:
    print(" You Guess it right You won!")
