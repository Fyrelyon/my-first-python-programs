# This program simulates a game of "Mad Libs"
#
# Gavin Bernard 8/28/2017
import time

print("Welcome to Mad Libs! Let's start off by entering a noun.")
noun1 = input()
time.sleep(2)

print("How about a second noun?")
noun2 = input()
time.sleep(2)

print("And a final noun?")
noun3 = input()
time.sleep(2)

print("Now, enter a verb.")
verb1 = input()
time.sleep(2)

print("A second verb?")
verb2 = input()
time.sleep(2)

print("One final verb.")
verb3 = input()
time.sleep(2)

print("Name a single adjective, a describing word.")
adjective = input()
time.sleep(2)

print("And how about a location?")
place = input()
time.sleep(2)

print(noun1 + " once told me the " + place + " is gonna roll me.")
print("I ain't the sharpest " + noun2 + " in the shed.")
print("She was looking kind of " + adjective + " with her finger and her thumb.")
print("In the shape of an L on her forehead.")

print("Well, the years start " + verb1 + " and they don't stop coming.")
print("Fed to the rules and I hit the " + place + " running.")
print("Didn't make sense not to live for fun.")
print("Your brain gets adjective but your " + noun3 + " gets dumb.")

print("So much to do, so much to see.")
print("So what's wrong with taking the " + place + "?")
print("You'll never " + verb2 + " if you don't go.")
print("You'll never " + verb3 + " if you don't glow.")

time.sleep(20)
