from sys import exit

f = open('day1/input.txt', 'r')
content = f.read()

updatedList = content.split("\n")

for num1 in updatedList:
    for num2 in updatedList:
        if int(num1) + int(num2) == 2020:
            print("Answer is: " +str( int(num1) * int(num2)))
            exit()
