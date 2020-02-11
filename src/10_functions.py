# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(number):
    if(number % 2 == 0):
        return True
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def even_or_odd(number):
    if(number % 2 == 0):
        print('even') 
    else:
        print ('odd')
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(even_or_odd(num))
