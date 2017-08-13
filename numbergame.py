import simpleguitk
import random 
import math

num = 100
anonymous_no = 0
guessleft = 0

def new_game():
	global num
	global anonymous_no
	global guessleft

	anonymous_no = random.randrange(0 , num)

	if num == 100:
		guessleft = 5
	elif num == 400:
		guessleft = 10

	print "New game.The range is from 0 to" , num 
	print "number of guess left is" , guessleft , "\n"
	pass
def range100():
	global num
	num = 100
	new_game()
	pass

def range400():
	global num
	num = 400
	new_game()
	pass

def input_guess(guess):
	global guessleft
	global anonymous_no

	won = False

	print "Your guess is:" , guess
	guessleft = guessleft - 1

	if int(guess) == anonymous_no:
		won = True
	elif int(guess) < anonymous_no:
		result = "guess something bigger"
	else:
		result = "guess something lower"

	if won:
		print "Correct guess dude!\n"
		new_game()
		return
	elif guessleft == 0:
		print "Sorry game is over!!!"
		new_game()
		return
	else:
		print result
		pass

f = simpleguitk.create_frame("Game:Guess the number!guys!" , 250, 250)
f.set_canvas_background("purple")

f.add_button("range is [0 , 100)" , range100 , 100)
f.add_button("range is [0 , 400)" , range400 , 400)
f.add_input("Enter the guess" , input_guess , 100)

new_game()
f.start()