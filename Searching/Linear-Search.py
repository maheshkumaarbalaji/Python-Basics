import random

def LinearSearch(InputList, n, ElementToBeSearched):
    try:
        isElementFound = False
        for i in range(n):
            if InputList[i] == ElementToBeSearched:
                print(f"{ElementToBeSearched} was found in InputList at position {i + 1}")
                isElementFound = True
        
        if isElementFound == False:
            print(f"{ElementToBeSearched} is not present in the InputList.")
    except Exception as err:
        print("LinearSearch(): An error has occured while performing search:", err)

InputArray = []
TotalCount = random.randint(1, 100)
print(f"There will be {TotalCount} numbers generated and added to the input list.")

for index in range(TotalCount):
    RandomNumber = random.randint(1, 1000)
    InputArray.append(RandomNumber)
    print(f"Element inserted at position {index + 1} of InputArray.")

RandomIndex = random.randint(1, 100) - 1
ElementToBeSearched = InputArray[RandomIndex]
print("The generated input list is", InputArray)
print("Element to be searched is", ElementToBeSearched)
LinearSearch(InputArray, TotalCount, ElementToBeSearched)