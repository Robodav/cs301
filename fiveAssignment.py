def insertionSort(unsorted):
    sortedlist = [unsorted[0]]
    unsorted.pop(0)
    for i in range(len(unsorted)):
        for j in range(len(sortedlist)):
            if sortedlist[j] >= unsorted[i]:
                sortedlist.insert(j, unsorted[i])
                break
            if j == len(sortedlist)-1:
                sortedlist.append(unsorted[i])
                break
    return sortedlist

def bubbleSort(unsorted):
    flag = True
    while flag:
        flag = False
        for i in range(len(unsorted)-1):
            if unsorted[i] > unsorted[i+1]:
                first = unsorted[i]
                unsorted[i] = unsorted[i+1]
                unsorted[i+1] = first
                flag = True
    return unsorted

def selectionSort(unsorted):
    print(unsorted)
    for i in range(len(unsorted)):
        largest = max(unsorted[:len(unsorted)-i])
        ind = unsorted.index(largest)
        unsorted[ind] = unsorted[-(i+1)]
        unsorted[-(i+1)] = largest
    return unsorted

def mergeSort(sorted1, sorted2):

def main():
    # print(insertionSort([5,3,2,4,1]))
    # print(insertionSort([12,98,100,2,9400,45]))
    # print(insertionSort([2,2,2,2,1,2]))
    # print(insertionSort([2]))

    # print(bubbleSort([5,3,2,4,1]))
    # print(bubbleSort([12,98,100,2,9400,45]))
    # print(bubbleSort([2,2,2,1,2]))
    # print(bubbleSort([2]))

    print(selectionSort([5,3,2,4,1]))
    print(selectionSort([12,98,100,2,9400,45]))
    print(selectionSort([2,2,2,1,2]))
    print(selectionSort([2]))

if __name__ == "__main__":
    main()
