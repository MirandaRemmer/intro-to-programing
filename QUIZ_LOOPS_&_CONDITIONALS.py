#MID-SESSION TAKE HOME QUIZ - LOOPS & CONDITIONALS 

#Miranda Remmer
#2.17

#1
def draw_square(num):
	for int in range (num):
		print "* " * num


draw_square(5)


#2
def draw_checkerboard():
	for grid in range (4):
		print ('X ' + 'O ') * 4
		print ('O ' + 'X ') * 4


print draw_checkerboard()