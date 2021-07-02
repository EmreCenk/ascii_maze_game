def print_character(where,x_coordinate,y_coordinate,name,x_values_of_line=[],x_values_of_new_line=[]):
	# The 'where' variable will be reffered to as 'c' from now on 
	c=where

	#The 'x_coordinate ' variable will be reffered to as 'space_number' from now on
	space_number=x_coordinate

	"""The 'where' will be a letter from w,a,s,d specfying where the character is trying to move. In order to move the character ,we first need to delete it. The following if statements calculates where the character is (with the variable 'x_coordinate' also known as 'space_number') and prints that many spaces for the character to not appear in the screen anymore. Immediately after, the character is printed at where it was trying to move. The if statements change the 'x_coordinate'/'space_number' and 'y_coordinate' to match the new character's coordinates. Almost all print statements end with \r in order to move the cursor to the beginning of the line to help clear it."""
	
	#Variable 'x_values_of_line' refers to the coordinates of spikes on the line the character is currently on. If character is on y=4, then 'x_values_of_line' would be a list of spikes on y=4
	#Variable 'x_values_of_new_line' refers to the same thing on the new line the character is trying to travel to. If the character is trying to go left or right, this array will be empty. If the character is trying to go up or down, this array will give the spike list of that new line.


	# Overall, the first layer of if statements will delete the character and change the y coordinate if needed.
	did_we_write_name=False
	
	if c=="d":
		#Changing the x coordinate
		space_number+=1

		#The following for loop goes through every single x coordinate and checks if there is a star on that coordinate. If there is, it places a star. If not, it places a space (it also checks if your character is on that coordinate as well).

		for i in range(0,133):
			if i==space_number:
				print(name,end="")
				did_we_write_name=True

			elif i in x_values_of_line:
				if did_we_write_name==True:
					i=i+len(name)+1
				print("*",end="")

			else:
				if did_we_write_name==True:
					i=i+len(name)+1
				print(" ",end="")
		print("",end="\r")


	elif c=="a":
		# The following if statement makes sure the space_number does not go under 0 (the game will start to have bugs if it goes under 0).
		if space_number>0:

			#Changing the x coordinate:
			space_number-=1

		# the following for loop does the same thing as the one at c=="d". It checks all x coordinates and reads what to put in them.
		for i in range(0,133):
			if i==space_number:
				print(name,end="")
				did_we_write_name=True

			elif i in x_values_of_line:
				if did_we_write_name==True:
					i=i+len(name)+1
				print("*",end="")

			else:
				if did_we_write_name==True:
					i=i+len(name)+1
				print(" ",end="")
		print("",end="\r")

	elif c=="s":
		#Checking the x coordinates and deciding what to put in them:
		for i in range(0,133):
			if i in x_values_of_line:
				print("*",end="")
			else:
				print(" ",end="")
	
		print("",end="\r")		
		#Changing the y coordinate:
		y_coordinate+=1

		# Since the character is trying to go down, we move on to the next line
		print()
		#After moving down, we do the exact same process to the new line, except this time we print the character when the cursor comes to the coordinate where the character is supposed to be.
		for i in range(0,133):
			if i==space_number:
				print(name,end="")
				did_we_write_name=True

			elif i in x_values_of_new_line:
				if did_we_write_name==True:
					i=i+len(name)+1
				print("*",end="")

			else:
				if did_we_write_name==True:
					i=i+len(name)+1
				print(" ",end="")
		print("",end="\r")

	elif c=="w":
		# Clearing the initial line the character was on:
		for i in range(0,133):
			if i in x_values_of_line:
				print("*",end="")
			else:
				print(" ",end="")
	
		print("",end="\r")	
		# Making sure y_coordinate does not go below 0:
		if y_coordinate>0:
			y_coordinate-=1

		#Since the character is trying to move up, we move to the line above:
		print("\033[F",end="\r")

		#We do the same process for the line that the character is trying to move to. We re-print everything but including the character this time.
		for i in range(0,133):
			if i==space_number:
				print(name,end="")
				did_we_write_name=True

			elif i in x_values_of_new_line:
				if did_we_write_name==True:
					i=i+len(name)+1
				print("*",end="")

			else:
				if did_we_write_name==True:
					i=i+len(name)+1
				print(" ",end="")
		print("",end="\r")

	# Since we had refered to x_coordinate as space_number, we need to change it back to its original name (this step has no practical use, I just thought it would be more aesthetically pleasing to see [x_coordinate,y_coordinate] instead of [space_number,y_coordinate] in the return statement):
	x_coordinate=space_number

	return [x_coordinate,y_coordinate]
def distinct_random_integers(how_many,interval_array):

	# This function generates 'how_many' number of integers between the interval 'interval_array'.
	
	#Disclaimer: There are far more efficient ways of doing this (For instance checking if 'how_many' is greater than numbers in the interval divided by 2.) but the purpose of this function does not need maximum efficiency. The program is quite simple. In fact we do not even need to check if the amount of numbers to generate is less than the numbers in the interval (in this program, that will always be true). But just in case I use this function for another program, I am making it so that there will never be an infinite loop.

	
	#Finding the numbers in the interval:
	numbers_in_interval=interval_array[1]-interval_array[0]+1

	#Checking to make sure enough integers are present in the given array to generate 'how_many' numbers:
	if how_many<numbers_in_interval:
		from random import randint
		
		# The numbers generated will be stored in this array:
		numbers_generated=[]

		# The loop will repeat 'how_many' times (aka generate 'how_many' numbers):
		for i in range(how_many):
			#The 'go_on' variable will only be False when a number that is not already generated becomes generated:
			# In other words, the loop will keep repeating until a unique number is generated
			go_on=True

			while go_on:
				new_num=randint(interval_array[0],interval_array[1])
				if new_num not in numbers_generated:
					numbers_generated.append(new_num)
					go_on=False
		return numbers_generated
	
	# If the 2 values are the same, we just return all integers between the array:
	elif how_many==numbers_in_interval:
		final=[]
		for i in range(interval_array[0],interval_array[1]+1):
			final.append(i)
		return final
	else:
		return False

def calculate_score(difficulty,time_taken):
	# The formula is (difficulty/(time_taken) )*100
	# This way the score is inversely proportional to the time_taken and directly proportional to the difficulty
	# By the way, this is the formula that computes something usefull (for your checklist)
	score=(difficulty/time_taken)*100
	return score
