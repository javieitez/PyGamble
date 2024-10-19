# enter 2 digits
try:
    firstNumber = int(input('Enter a Number: '))
    secondNumber = int(input('Enter another Number: '))
except:
    print('Must be a Number')

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


