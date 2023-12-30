import random

def InsertionSort(InputList, n, SortingOrder = "asc"):
    try:
        for i in range(1, n):
            j = i - 1
            temp = InputList[i]
            if SortingOrder == "asc":
                while j>= 0 and InputList[j] > temp:
                    InputList[j + 1] = InputList[j]
                    j = j - 1
                InputList[j + 1] = temp
            elif SortingOrder == "desc":
                while j>= 0 and InputList[j] < temp:
                    InputList[j + 1] = InputList[j]
                    j = j - 1
                InputList[j + 1] = temp
    except Exception as err:
        print("InsertionSort(): An error occurred while sorting input list:",  err)

InputArray = []
TotalCount = random.randint(1, 100)
print(f"There will be {TotalCount} numbers generated and added to the input list.")

for index in range(TotalCount):
    RandomNumber = random.randint(1, 1000)
    InputArray.append(RandomNumber)
    print(f"Element inserted at position {index + 1} of InputArray.")

print("Input Array Contents before sorting:", InputArray)
InsertionSort(InputArray, TotalCount)
print("Input Array contents after sorting in ascending order:", InputArray)