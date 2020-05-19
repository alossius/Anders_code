
#Type:
#
#	Primitive Types:
#		- int: store integers
#		- floats/doubles: store doubles
#		- booleans: true and false
#		- strings: collections of characters
#
#	Reference Types:
#		- lists: collection of variables

#Python and Type: Python guesses what the type is. In a language like Java you have to always state the type. 


#Casting: Casting is changing the type

num = 6 #this is an integer
name = "Paul" #this is a string
school = "Upper Canada Collge" #this is a string
address = "220" #this is also a string - the computer has no idea this is a number
height = 188.43 #this is a float

num = num + 1
print(num)

address = address + "1"
print(address)

nums = [1,4,6,7,8] #This is a list of nums
names = ["Paul","Simon","Troy"] #This is a list of names
heights = [190.23,67.45,167.66] #This is a list of heights

#How do I access parts of the list?
#The two things you should always think about when working with lists
    #Lenght and Index
# 0 1 2 3 4 5. --> Indexs are 0 - 5
#[1,4,6,7,6,8] --> Lenght = 6

print(nums)
print(nums[0]) #says "nums at 0"
print(nums[1]) 

#Length and indexes are essntial strings as well

#       012345
word = "monkey" #lengh = 6
print(word) #gives "monkey"
print(word[0]) #gives "m"
print(word[1]) #gives "o"

word1 = "fish cakes" #length = 10 indexes: 0-9
#taking imputs
#you can use the indexing to pull out parts of strings of parts of lists
print(word[5:10]) #this is called a substring [index-inclusive : index-exclusive]

#To take inputs you use an input functions
var1 = input("Enter your name: ")
print("Your name is",var1) #you can use comma regardless

age = input("How old are you: ")
#Before using the variable as an integer we need to CAST it. Casting is the process of changing the tpe.
age = int(age) #casts age to an integer
age = age + 5
print("In 5 years you will be",age,"old")

### PYTHON TAKES EVERYTHING AS A STRING ###