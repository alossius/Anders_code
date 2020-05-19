

x = 2

if (x == 2):
    print("X = 2")

print("*************")

'''
# count from -10 to 100
ctr = -10;
while (ctr < 100):
    print("ctr = ",ctr)
    ctr = ctr + 1

# count from 1 to 10
ctr = 1;
while (ctr < 10):
    print("ctr = ",ctr)
    ctr = ctr + 1
'''

# write this in one line ^^

    # with numbers: 
for i in range(0,10,1):
    print(i)

# HOW DOES IT WORK?::
#    range(<count>,<check>,<range>)
    # i = 0 | 0 < 5 | TRUE --> RUN LOOP i = i + 1 = 0 + 1 = 1
    # i = 1 | 1 < 5 | TRUE --> RUN LOOP i = 2
    # i = 2 | 2 < 5 | TRUE --> RUN LOOP i = 3
    # i = 3 | 3 < 5 | TRUE --> RUN LOOP i = 4
    # i = 4 | 4 < 5 | TRUE --> RUN LOOP i = 5
    # i = 5 | 5 < 5 | FALSE --> EXIT LOOP
    
    # with a string

print("******************")

str = "anders"
for i in range(0,len(str),1):
    print(str[i])