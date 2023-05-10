def bubbleSort(numberArray):
    for i in range(len(numberArray)):
        for j in range(len(numberArray)):
            if numberArray[i] < numberArray[j]:
                tempNumber = numberArray[i]
                numberArray[i] = numberArray[j]
                numberArray[j] = tempNumber
    return numberArray

def reverseString(text):
    textArray = list(text)
    result = [None]*len(textArray)
    for i in range(len(textArray)):
        result[i] = textArray[len(textArray) - (i + 1)]
    return ''.join(result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(bubbleSort([20, 1, 7, 20, 3, 2]))
    print(reverseString('Nexla'))

