## Part 1 ##

'''
The range() function is used to generate a sequence of numbers. However, the code snippet provided below does not work as intended. Your task is to identify why the loop might not be executing and correct the code so that it prints numbers from 5 down to 3.
Write a program that simulates different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.
Create a countdown timer that starts from 10 and counts down to 1. Use the range() function to generate the countdown sequence. Each number should be printed on a new line. This task will help you understand how to generate a decreasing sequence with range().
'''

for i in range(5, 2, -1):
    print(i)

import random
moods = ["Happy", "Sad", "Energetic", "Calm"]
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
week_days_index = range(len(week_days)) #using range seems unnecessary if you spell out the days.
for days in week_days_index: 
    print(week_days[days] +": " + random.choice(moods) +". ", end="" +"\n") # I wanted to use formatting to make this clean.

for i in range(10, 0, -1): 
    print(i)

## Part 2 ##
''' 
The code below is intended to print a 3x3 grid of asterisks. However, the current output is not as expected. Identify the logical errors in the nested loops and correct the code so that it prints the grid correctly, with each row of asterisks on a new line.
Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it.
Your task is to create a multiplication table for numbers 1 through 5. Use nested loops where the outer loop represents the multiplier and the inner loop represents the multiplicand. Print the results in a tabular format.
'''
for i in range(3):
    print("***")
    print("\n")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times = ["Morning", "Afternoon", "Evening"]
moods2 = ["Happy", "Sad", "Scared"]

for day in days: 
    for time in times:
        print(f"{day}: {time}: {random.choice(moods2)}")

multiplication_table = range(1, 6)
for multiplier in range(1,6): 
    for multiplicand in range(1,6):
        product = multiplicand * multiplier
#        print(product) # I've never heard the word tubular. Below is best shot.
        print(product, end = "\t")

## Part 3 ##
        
'''
The loop below is meant to print all numbers from 1 to 10, but it stops prematurely due to a break statement. Correct the code so that it skips over the number 5 and continues to print the rest of the numbers.
Write a program that represents your mood swings throughout a day. The program should loop over each hour of the day and assign a random mood from a list for each hour. However, at 'lunchtime' (which you can define as a specific hour), the program should not print the mood. Use the continue statement to achieve this behavior.

Implement a for loop that searches for a specific number in a list of numbers. If the number is found, use break to exit the loop. If the loop completes without finding the number, an else clause should be used to print a message stating that the number was not found. This task will help you understand how to use the else clause in conjunction with the break statement in loops.
Write a program that represents your mood swings throughout a day. The program should loop over each hour of the day and assign a random mood from a list for each hour. However, at 'lunchtime' (which you can define as a specific hour), the program should not print the mood. Use the continue statement to achieve this behavior.

Implement a for loop that searches for a specific number in a list of numbers. If the number is found, use break to exit the loop. If the loop completes without finding the number, an else clause should be used to print a message stating that the number was not found. This task will help you understand how to use the else clause in conjunction with the break statement in loops.
'''

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

mood3 = ("Happy", "Sad", "Frustrated")
lunchtime = 12
for hour in range(1, 24 +1, 1):
    if hour == lunchtime:
        continue
    else:
        print(str(hour) + (" ")  + random.choice(mood3)) # I was having trouble but hour needed to convert to str from int

#This will select random numbers from a range. Some will be present in list, some wont.
loop_range = list(range(1, 10, 1))
search_for = random.randint(1, len(loop_range) + 5)
for number in loop_range:
   if number == search_for:
       print((str(search_for)) + " found!")
       break
else:
    print((str(search_for)) + " not found!")

## Part 4 ##
'''
Given the following code snippet, predict the output and then run the code to verify your prediction. Explain why the output is what it is based on the placement of the increment operation. 
Modify the code from Task 1 by moving the increment operation to the end of the loop. Predict what the output will be and then run the code to check your prediction. Discuss the differences in the output and how the placement of the increment affects the loop's behavior.
Create a while loop where an off-by-one error could occur due to the placement of the increment operation. Your loop should aim to fill a bag with exactly 10 marshmallows, but due to the off-by-one error, it either has too few or too many. Correct the error and explain the importance of increment placement in preventing such errors.

Modify the code from Task 1 by moving the increment operation to the end of the loop. Predict what the output will be and then run the code to check your prediction. Discuss the differences in the output and how the placement of the increment affects the loop's behavior.
'''

# I expect this code to add one until it reaches five and print the message.
# That's what happened!

# If we run this modified code it will display the message before adding, so the count in the message will be off.
# The message wont display once we hit 5
'''marshmallows = 0
while marshmallows < 5:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1'''
# Thats what happened!

marshmallows = 0
while marshmallows < 10:
    print("there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1

marshmallows = 0
while marshmallows < 10:
    marshmallows += 1
    print("there are " + str(marshmallows) + " marshmallows.")

# It is so important to place the increment in the right place. 
# The whole count is thrown off if you don't
    
## Part 5 ##
    
''' 
(note typo, should say "always be true") Write a while loop with a condition that will never be true (an infinite loop). Inside the loop, print a statement. Then, use a break statement to exit the loop after 5 iterations. Explain the role of the loop condition and the break statement in controlling the loop execution.

Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. The loop should terminate naturally once the condition is met. Discuss how the loop condition determines when the loop exits.

'''
crash = True 
iterations = 0

while crash == True:
    print("this loop will crash if you are not careful " + "iteration count, " + str(iterations + 1)) 
    iterations += 1
    if iterations >= 5:
        print("five iterations, ending loop")
        break

crash = 0 
iterations = 0
while crash <= 5:
    print("this loop will crash if you are not careful " + "iteration count, " + str(iterations + 1)) 
    iterations += 1
    crash += 1

crash = 2 
fall = 1
iterations = 0
while crash <= 5 and crash >= 2 or fall < 7:
    print("this loop will crash if you are not careful " + "iteration count, " + str(iterations + 1)) 
    iterations += 1
    crash += 1
    fall += 1
# This is just a small modification to run while only two conditions are present
# You can combine conditions to create complex scenarios. 
# Maybe you only want to display a warning message while the winds are over a certain speed and the expected rain is over a certain amount. 

## Part 6 ##
    
'''
Write a while loop that attempts to find a specific value in a list. Use an else clause to print a message if the value is not found. Explain how the else clause works with the while loop.

Create a while loop that runs indefinitely, printing out the current time. Use a break statement to exit the loop if a certain condition is met (e.g., if the current time matches a target time). Discuss how the break statement can be used to exit a loop based on a condition.

Develop a while loop that iterates over a range of numbers. Use the continue statement to skip over specific numbers (e.g., multiples of 3) and print the rest. Explain the purpose of the continue statement and how it affects the loop's iteration.

Implement a while loop where you want to temporarily skip the implementation of a condition but plan to add more code later. Use the pass statement as a placeholder. Describe the use of pass in a loop and when it might be useful.
'''

# This is modified from the code I wrote above. 
# Here while search_for is in loop range, it will print, and break the loop
# Else is a fall back, if search_for is not in range, it will print a different message
loop_range = list(range(1, 10, 1))
search_for = random.randint(1, len(loop_range) + 5)
while search_for in loop_range:
       print((str(search_for)) + " found!")
       break
else:
    print((str(search_for)) + " not found!")

import datetime

while True:
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if hour < 23:
        print("not time yet!")
        break
    if hour >= 23:
        print("It's time!")
        break
    

# Here, this loop would run indefinitely without the breaks. 
# The break is the only thing that ends the loop. 

point = 0
while point < 13:
    point += 1
    if point % 3 == 0:
        continue
    print("point = " + str(point))
# Continue skips the number from printing if the point is divisible by 3.  
    
point = 0
while point < 13:
    point += 1
    if point % 3 == 0:
        pass
    print("point = " + str(point))
# Using the same code as above, pass in place of continue lets the program run while including a placeholder for a later function.

## Part 7 ##
    
'''

Using the provided code snippet, simulate rolling a six-sided die 10 times. Extend the simulation to keep track of how many times each number is rolled. After the simulation, print out the frequency of each number.
Create a game where a player has to guess the random item picked by the computer from a list. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.
Simulate shuffling a deck of cards using random.shuffle(). Create a list representing a deck of cards, then shuffle it and print the shuffled deck. Discuss how random.shuffle() can be used in game development or other applications.
'''

## This code was all completely done already. I worked from the example. ##
import random


roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


for _ in range(10):
    dice_roll = random.randint(1, 6)
    roll_count[dice_roll] += 1
    print("You rolled a " + str(dice_roll) + "!")

for number, frequency in roll_count.items():
    print(f"Number {number} was rolled {frequency} times.")

choice_list = ["red", "blue", "yellow"]
user_guess = input("what do you think the computer will guess? ")
choice = random.choice(choice_list)
if choice == user_guess.lower():
    print("You guessed correctly! The computer picked " + choice + " ")
elif choice != user_guess.lower():
    print(" Too bad, the computer picked " + choice +" ")

cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, "Jack", "Queen", "King"]
random.shuffle(cards)
print(cards)
# You could use shuffle in game development like in the example above, to shuffle a card game. 
# You could also use it too shuffle a list of items in a lottery and them make the user blind pick one of them.

## Part 8 ##

''' 
Implement a number guessing game where the computer randomly selects a number within a range, and the player has to guess it. Use random.randint() to generate the number and give the player a hint after each incorrect guess whether their guess was too high or too low.

Create a Magic 8-Ball program that provides random advice. Use random.choice() to select a random response from a list of possible answers every time the user asks a question.

Develop a game where the computer randomly picks a card from a deck, and the player has to guess the suit or the rank. Use random.choice() to select the card, and then check if the player's guess matches the suit or rank of the chosen card.
'''

user_guess = int(input("What number will the computer guess between 1 and 10? "))
choice = random.randint(1, 10)
if choice == user_guess:
    print("You guessed correctly! The computer picked " + str(choice) + " ")
elif choice != user_guess:
    print(" Too bad, the computer picked " + str(choice) +" ")

## Part 9 ##
'''
Using the provided genres list, write a for loop that prints out each genre with a custom message. Extend this task by adding a counter that displays the number of the track before the genre.
Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but also includes a condition to stop the loop if a certain genre is played.
Using the range() function, loop through the genres list by index. For each genre, print out the track number and a message that the light show is ready. Modify the loop to skip a genre if it's not suitable for the light show.

'''  
# Worked off the example code but decided to make changes
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track_number = 1
first_track = 0
for genre in genres:
    print(f"Track {track_number}: Now playing {genre}")
    track_number += 1
stop_genre = 'Rock'
while first_track < len(genres) and genres[first_track] != stop_genre:
    print("Remixing: " + genres[first_track])
    first_track += 1
unsuitable_genre = "Jazz"
hardest_genre = "Classical"
for genre_index in range(len(genres)):
    if genres[genre_index] == unsuitable_genre:
        continue
    elif genres[genre_index] == hardest_genre:
        print("Track 4: Classical: Mega Light Show!")
    else:
        print(f"Track {genre_index + 1}: {genres[genre_index]} - Light show is on!")

## Part 10 ##
        
'''
Loop through a slice of the genres list and print only the selected genres. Use slicing to create a sublist of genres from the second to the fourth track.

Use a list comprehension to create a new list that contains each genre with the word "Music" appended to it. Print this new list.

Write a loop using range() to print out a countdown from 10 to 1, followed by the message "The beat drops now!".
'''
## I also worked off the example for this question ##
short_genres = genres[1:4]
for genre in short_genres:
    print("New play: " + genre)
music_genres = [genre + " Music" for genre in genres]
print(music_genres)
for number in range(3, 0, -1):
    print(number)
print("The beat drops now!")