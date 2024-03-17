def main():
    # Create an array, initialised with a few values
    numbers = [4, 3, 7, 2, 8]

    # Let's find out the length of the array
    arrayLength = len(numbers)
    print (f'The array is {arrayLength} items long and the first item is {numbers[0]}')

    # Let's add another value to the end of the array
    newValue = int(input('Another value to add: '))
    numbers.append(newValue)

    arrayLength = len(numbers)
    print (f'The array is now {arrayLength} items long and the first item is {numbers[0]}')

    total = 0

    # Loop over each item in the array
    for num in numbers :
        total = total + num

    average = total / len(numbers)

    print (average)

    # We can also just print the array
    print (numbers)
main()
