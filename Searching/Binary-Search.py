import random

def BinarySearch(InputList, n, ElementToBeSearched):
    try:
        l, r = 0, n - 1
        while l <= r:
            m = (l + r)//2
            if InputList[m] == ElementToBeSearched:
                print(f"{ElementToBeSearched} was found in InputList at index {m}")
                break
            elif ElementToBeSearched > InputList[m]:
                l = m + 1
            elif ElementToBeSearched < InputList[m]:
                r = m - 1
    except Exception as err:
        print("BinarySearch(): An error occurred while performing search:", err)

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
InputArray = sorted(InputArray)
print("Sorted list needed for binary search of element is:", InputArray)
print("Element to be searched is", ElementToBeSearched)
BinarySearch(InputArray, TotalCount, ElementToBeSearched)