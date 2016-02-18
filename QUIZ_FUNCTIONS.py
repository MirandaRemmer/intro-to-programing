#MID-SESSION TAKE HOME QUIZ - FUNCTIONS 

#Miranda Remmer
#2.17


#1
def convert_to_seconds(hours, minutes, seconds):
	min_to_seconds = int(minutes * 60)
	hours_to_seconds = int(hours * 3600)
	total_seconds = min_to_seconds + hours_to_seconds + seconds
	return total_seconds


print "CONVERT TIME TO SECONDS!"
hours = int(raw_input("How many hours? "))
minutes = int(raw_input("How many minutes? "))
seconds = int(raw_input("How many seconds? "))


output = convert_to_seconds(hours, minutes, seconds)
print "%r hours, %r minutes, and %r seconds is %i seconds!" % (hours, minutes, seconds, output) 




#2
def convert_to_inches (feet, inches):
	feet_to_inches = int(feet * 12)
	total_inches = feet_to_inches + inches
	return total_inches



print "CONVERT FEET TO INCHES!"
feet = int(raw_input("How many feet? "))
inches = int(raw_input("How many inches? "))


output = convert_to_inches(feet, inches)
print "%r feet and %r inches is %i inches!" % (feet, inches, output) 