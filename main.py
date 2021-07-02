from getch import *
from time import sleep
from random import randint
from time import perf_counter
from Functions import *

#From the Functions folder I will be using the Functions 'calculate_score','print_character' and 'distinct_random_integers'. I have written these functions myself and you can read them by clicking to the left of the screen and clicking on the 'Functions.py' folder. The reason I made 2 different folders is to make the main loop more organised. I believe this way the code is much easier to read and write.

# I refer to stars as spikes and vice versa throughout the code. 
# Stars/spikes are the things you try to not bump into

#Setting the initial x and y values of the character:
x=1
y=1

#Welcome message:
print("Hello, welcome to the obstacle course game! You will be controlling a character on a 2 dimensional field.\n\nUse the w,a,s and d keys to move around. If you step on any stars, you lose the game.\n\nThe purpose of this game is to cross from the left side of the screen to the right side without stepping on any stars.\nThe only rule is, you can only see the star pattern of a line once you visit it.\nOnce you explore a line, only then you can see the star pattern.\n\nWarning: If you try to go around the stars by making the character go down as far as possible, you will be automatically killed.\nThe top barrier of stars is visible but the bottom layer of barrier stars are invisible.\nBe carefull, if you go down more than 25 times, the invisible barrier will kill you off.\nSo it would not be advised to not spam going down.\nThe same thing applies if you try to make the character go above where you spawn (except this time, the barrier is visible. \n\nNote: In order to play this game, you must choose your repl it layout to be 'stacked' (you can do this from the settings in the left). \nAfter doing so, stretch the screen as much as possible horizontally.\nAs a test, look at the following straight line of stars. \n\nIf you see them as 1 straight line, then you're screen is good to go. \nIf you see 1 line of stars stretching across the screen and 1 line of shorter stars under it, keep stretching your screen.\nOnce you see the stars as 1 single line, you can proceed.\n")
print("*"*133)

# The while loop makes sure the username is 1 letter. We will set a dummy name value for the loop to start
name="aa"

# 'n' will be used to count how many times the user has been asked. This variable will be used to clear out all the lines asking the user for their username ( n is already 9 because we have already have 9 lines to clear out)
n=16
print()
while len(name)>=2:
	
	print("Pick a username (your username must be 1 letter, it can be any letter, number or symbol) : ")
	name=input()
	n+=1

#Difficulty goes up to 24. The 'difficulty' variable sets how dense the stars are going to be. 24 difficulty means on average,  24 out of the 25 y values will have spikes (more on generating levels later. For now, all you need to know is difficulty=spike density.

Finish=False
while Finish==False:
	print("Pick a difficulty. The difficulty goes from 1 to 24 (inclusive). ")
	difficulty=input()

	#We add 1 to n since we have 1 more line to clear now
	n+=1

	try:
		#Here we test if what the user entered is an integer. If not, the while loop asks them again
		difficulty=int(difficulty)

		#At this point we know the user has entered an integer
		if 1<=difficulty<=24:
			Finish=True

		else:
			print("You need to enter a number between 1 and 24 inclusive")
			#We add 1 to n since we have 1 more line to clear now
			n+=1
	except ValueError:
		print("Please enter an integer. ")
		n+=1
print("When you press enter, the timer will begin. After pressing enter, press w,a,s or d for your character to appear ")
input()
n+=1

# Clearing all lines where the user is asked to enter their username in:
for i in range(n):
	# The string "\033[F" takes the cursor up
	print("\033[F"+" "*133,end="\r")

#The max y value will be 25, if the player attempts going further, he will be killed
#The maximum x value will be 132. If the player reaches it, they win.




vertical_spikes=[]
coordinates_of_spikes=[]

# Generating vertical spikes with 6 letters of empty space in between:
for i in range(1,22):

	#Generating distinct integers for the y coordinates:
	distinct_y_coordinates=distinct_random_integers(difficulty,[1,25])

	for j in distinct_y_coordinates:
		#Appending the coordinates with 6 spaces between:
		vertical_spikes.append([i*6,j])

# We will now group all vertical spike coordinates depending on their y value in a dictionary. The y value will be the key and the corresponding x coordinates will be the value (in other terms, we write down what x values the spikes have for each y coordinate).After doing so , we will sort the corresponding x values in ascending order. The end result will look like {y1:[x(highest),x2,x3...x(lowest)],y2:[x(high),x12,x23,x32...x(low)}
# (The purpose of doing this is to make printing the spikes/stars onto the screen possible. If the x values are not sorted in ascending order, we cannot print them onto the screen. Also, since the y values are grouped, for collision detection, all we need to do is check the y value that the character is on. If we did not do this, we would need to check every single spike, every single turn.)


#Converting everything to a dictionary:
coordinate_dictionary={}
for i in vertical_spikes:
	# i[0] is the x coordinate
	# i[1] is the y coordinate

	if i[1] not in coordinate_dictionary:
		# If the y value is not in the dictionary yet, we add a key with that y value
		coordinate_dictionary[i[1]]=[i[0]]
	else:
		# If the y value is already in the dictionary, we append the corresponding x value
		coordinate_dictionary[i[1]].append(i[0])

#Ordering all x values in the dictionary:
updated_dictionary={}

for i in coordinate_dictionary:
	# Sorting the x values and the new keys and values to updated_dictionary:
	# We use the python's in built 'sorted()' function to sort the x values.
	sorted_x_values=sorted(coordinate_dictionary[i])
	updated_dictionary[i]=sorted_x_values

#Updating the coordinate dictionary:
coordinate_dictionary=updated_dictionary

#We need to add 2 horizontal barriers at y=0 and y=26. The first one will be visible, the second one will be invisible.

#Adding barrier at y=0
coordinate_dictionary[0]=[]
for i in range(1,133):
	coordinate_dictionary[0].append(i)

coordinate_dictionary[26]=[]

#Adding barrier at y=26
for i in range(1,133):
	coordinate_dictionary[26].append(i)



#The variable keep_going will only become false when the player looses or the game finishes
keep_going=True

#This is the main loop:
print("\nYour time starts now. Good luck.")
print("*"*132)

#Starting the time:
t_initial = perf_counter()


while keep_going==True:
	
	# The getch() function is used to get 1 letter inputs from the user without showing it
	# as text
	c=getch()

	#If c is s or w, than that means the y value is going to change. If this is the case we need to check if there are any spikes on the new y value. If so, we need to enter those x values into the function 'print_character' for it to print the correct stars on the new y value as well.
	if c=="s" and (y+1) in coordinate_dictionary:
		next_line_spikes=coordinate_dictionary[y+1]
	elif c=="w" and (y-1) in coordinate_dictionary:
		next_line_spikes=coordinate_dictionary[y-1]
	else:
		next_line_spikes=[]
		

	# We need to check if the y line the character is on has any spikes on it. If the person chose a lower difficulty, then there may not be any spikes on the line
	if y in coordinate_dictionary:
		#There are spikes, the coordinates are coordinate_dictionary[y]
		coordinates=print_character(c,x,y,name,coordinate_dictionary[y],next_line_spikes)
	else:
		# There are no spikes in this y value. We do not have to enter anything since the default value for spikes is an empty array.
		coordinates=print_character(c,x,y,name,x_values_of_new_line=next_line_spikes)
		

	#Updating the x and y values:
	x=coordinates[0]
	y=coordinates[1]

	# We will now check if there is any overlap between any spikes and The character 
	if y in coordinate_dictionary and x in coordinate_dictionary[y]:
		keep_going=False

		#since the person has lost:
		win=False
		break
	elif x==132:
		# At this point we know the character is not an a spike, now we will check if it's x value is at the finish line (x=132)
		keep_going=False
			
		#Since the person has won:
		win=True
		break

# Finishing timer:
t_final = perf_counter() #The perf_counter function gives us the amount of time passed relative to an unspecified time (as a benchmark). But since both the initial and final are relative to the same time, their differences must be the time passed in seconds.

#Calculating total time passed:
total = t_final-t_initial

if win==False:
	print("\n\n\n\n\n\nYou bumped into a star.\nYou have lost the game.")
	input("\nPress enter to finish session.")
else:
	print("\n\n\n\n\n\nYou have won the game.")
	input("\nPress enter to proceed.  ")
	#Clearing out all the lines that have been printed:
	for i in range(50):
		print("\033[F"+" "*133,end="\r")

	high=input("Would you like to be featured in the High_Scores list? (y/n) ")
	if high in ["yes","YES","Yes","y","Y"]:
		# We place a dummy value for 'newname' to start the while loop 
		# Until the user enters in the correct number of letters, the loop will keep going
		newname="d"
		while len(newname) not in [4,5,6,7]:
			newname=input("What would you like your displayed name to be? (minimum 4 characters, maximum 7 characters): ")
			
		folder=open("High_Scores","a")

		#The high scores file is not sorted since not many people will play the game. It is more like a display of people who have played rather than a high score list.
		# I know the following snippet may be hard to read but basically I take their name, round their time, and round their score to the nearest ten. Then I write that information to the High_Scores folder
		
		folder.write("\n"+newname+"				"+str(difficulty)+"				"+str(round(total,1))+"			 "+str( round( calculate_score(difficulty,total),1  ))  )  

		folder.close()

		print("It took you " + str(total) + " seconds to finish the game. Well played.")
