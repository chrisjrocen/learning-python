'''
A program to convert miles to kilometres

Kilometres = Miles * 1.60934
'''
# Ask for input 

miles = input('Enter the number of miles')

# convert string to interger

miles = int(miles)

# Make culacuation 

km = miles * 1.60934

# PRovide output

print ("{} miles = {} kilometres".format(miles, km))