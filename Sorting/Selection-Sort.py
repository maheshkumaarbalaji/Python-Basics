import random

def SelectionSort(InputList, n, SortingOrder = "asc"):
    try:
        for i in range(n - 1):
            key = InputList[i]
            index = i
            for j in range(i + 1, n):
                if SortingOrder == "asc":
                    if InputList[j] < key:
                        key = InputList[j]
                        index = j
                elif SortingOrder == "desc":
                    if InputList[j] > key:
                        key = InputList[j]
                        index = j
            if index != i:
                (InputList[i], InputList[index]) = (InputList[index], InputList[i])
    except Exception as err:
        print("SelectionSort(): An error occurred while sorting input list:", err)
InputArray = []
TotalCount = random.randint(1, 100)
print(f"There will be {TotalCount} numbers generated and added to the input list.")

for index in range(TotalCount):
    RandomNumber = random.randint(1, 1000)
    InputArray.append(RandomNumber)
    print(f"Element inserted at position {index + 1} of InputArray.")

print("Input Array Contents before sorting:", InputArray)
SelectionSort(InputArray, TotalCount)
print("Input Array contents after sorting in ascending order:", InputArray)