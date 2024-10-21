################################################################
#
# Enter two numbers, then some operations are performed on them
#
################################################################

# enter 2 digits
a = b = False
while a == False:
    c = input('Enter a Number: ')
    firstNum = int(c)
    a = c.isdigit()
while b == False:
    c = input('Enter another Number: ')
    secondNum = int(c)
    b = c.isdigit()

#Compare which one is bigger
if firstNum > secondNum:
    print(firstNum, 'is bigger than', secondNum)
    biggerNum = firstNum
    lesserNum = secondNum
elif firstNum < secondNum:
    print(secondNum, 'is bigger than', firstNum)
    biggerNum = secondNum  
    lesserNum = firstNum
elif firstNum == secondNum:
    print(firstNum, 'and', secondNum, 'are exactly the same')
    biggerNum = firstNum
    lesserNum = secondNum

# Sum  and multiply the two digits
print('The sum of', firstNum, 'and', secondNum, 'is', (firstNum + secondNum))
print(firstNum, 'times', secondNum, 'is', (firstNum*secondNum))

# Divide with decimals
print(biggerNum,'divided by', lesserNum,'is', (biggerNum / lesserNum))

# exponentiate
print(biggerNum, '**', lesserNum, 'is', biggerNum**lesserNum)
print('same as multiplying', lesserNum, 'by itself', biggerNum, 'times')
