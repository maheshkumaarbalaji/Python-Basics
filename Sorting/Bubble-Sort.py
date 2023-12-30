import random

def BubbleSort(InputList, n, SortingOrder = "asc"):
    try:
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if SortingOrder == "asc":
                    if InputList[j] > InputList[j + 1]:
                        (InputList[j], InputList[j + 1]) = (InputList[j + 1], InputList[j])
                elif SortingOrder == "desc":
                    if InputList[j] < InputList[j + 1]:
                        (InputList[j], InputList[j + 1]) = (InputList[j + 1], InputList[j])
    except Exception as err:
        print("BubbleSort(): An exception occurred while sorting the input list:", err)

InputArray = []
TotalCount = random.randint(1, 100)
print(f"There will be {TotalCount} numbers generated and added to the input list.")

for index in range(TotalCount):
    RandomNumber = random.randint(1, 1000)
    InputArray.append(RandomNumber)
    print(f"Element inserted at position {index + 1} of InputArray.")

print("Input Array Contents before sorting:", InputArray)
BubbleSort(InputArray, TotalCount)
print("Input Array contents after sorting in ascending order:", InputArray)