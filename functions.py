
def do_this():
    print("Doing this!")

#def is short for define - it means define a function

#def <name of function>: 
    # - In python we seperate words with a _
    # - Function names are always spelt with a lower case: This is a clue to anyone reading the code

#You can invoke a function by typing its name

# A return statement is what the function gives back

def add_numbers(a, b):
    print("Running add_numbers")
    return a + b

print("What is a function")
do_this()
print("Continuing")
x = add_numbers(1,2)
print(x)

# You can write you own functions
