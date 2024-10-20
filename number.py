# enter 2 digits
a = b = False
while a == False:
    c = input('Enter a Number: ')
    firstNumber = int(c)
    a = c.isdigit()
while b == False:
    c = input('Enter another Number: ')
    secondNumber = int(c)
    b = c.isdigit()

#Compare which one is bigger
if firstNumber > secondNumber:
    print(firstNumber, 'is bigger than', secondNumber)
    biggerNumber = firstNumber
    lesserNumber = secondNumber
elif firstNumber < secondNumber:
    print(secondNumber, 'is bigger than', firstNumber)
    biggerNumber = secondNumber  
    lesserNumber = firstNumber
elif firstNumber == secondNumber:
    print(firstNumber, 'and', secondNumber, 'are exactly the same')
    biggerNumber = firstNumber
    lesserNumber = secondNumber

# Sum  and multiply the two digits
print('The sum of', firstNumber, 'and', secondNumber, 'is', (firstNumber + secondNumber))
print(firstNumber, 'times', secondNumber, 'is', (firstNumber*secondNumber))

# Divide with decimals
print(biggerNumber,'divided by', lesserNumber,'is', (biggerNumber / lesserNumber))

# exponentiate
print(biggerNumber, '**', lesserNumber, 'is', biggerNumber**lesserNumber)
print('same as multiplying', lesserNumber, 'by itself', biggerNumber, 'times')
