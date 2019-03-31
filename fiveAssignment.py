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
    print(sorted1)
    print(sorted2)
    combined = []
    if len(sorted1) >= len(sorted2):
        largest = sorted1
        smallest = sorted2
    else:
        largest = sorted2
        smallest = sorted1
    difference = len(largest) - len(smallest)
    for i in range(len(smallest)):
        if smallest[i] <= largest[i]:
            combined.append(smallest[i])
            combined.append(largest[i])
        else:
            combined.append(largest[i])
            combined.append(smallest[i])
    for j in range(len(smallest),len(largest)):
        combined.append(largest[j])
    return combined

def main():
    #---------Insertion Sort----------#
    # print(insertionSort([5,3,2,4,1]))
    # print(insertionSort([12,98,100,2,9400,45]))
    # print(insertionSort([2,2,2,2,1,2]))
    # print(insertionSort([2]))
    
    # The worst case Big Oh running time for insertion sort is O(n^2). This is because
    # the main for loop will always run in n time, while the nested will also build up
    # to a length of n. It may appear to be O(n^3) because there is an insert method
    # in the nested loop, however these two linear functions are mutually exclusive.
    # If the insertion is done at the first spot in the sorted list, the sorted list won't
    # have been traversed, so the only linear method will have been the insert.

    #---------Bubble Sort---------#
    # print(bubbleSort([5,3,2,4,1]))
    # print(bubbleSort([12,98,100,2,9400,45]))
    # print(bubbleSort([2,2,2,1,2]))
    # print(bubbleSort([2]))

    #

    # print(selectionSort([5,3,2,4,1]))
    # print(selectionSort([12,98,100,2,9400,45]))
    # print(selectionSort([2,2,2,1,2]))
    # print(selectionSort([2]))

    # print(mergeSort([1,3,5],[2,4,6]))
    # print(mergeSort([1,50,100],[2,49,70,110,120,130]))
    # print(mergeSort([2],[1]))

if __name__ == "__main__":
    main()
