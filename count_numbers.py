num1 = input("Input a number ")
num1 = int(num1)

num2 = input("Input another number ")
num2 = int(num2)

small = min(num1,num2)
large = max(num1,num2)

small = int(small)
large = int(large)

for i in range(small, large + 1, 1):
    print (i)
