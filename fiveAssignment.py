######################################
# David Vandiver                     #
# CS301                              #
# Assignment 5 - Sorting Lists       #
######################################

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
    for i in range(len(unsorted)):
        largest = max(unsorted[:len(unsorted)-i])
        ind = unsorted.index(largest)
        unsorted[ind] = unsorted[-(i+1)]
        unsorted[-(i+1)] = largest
    return unsorted

def mergeSort(sorted1, sorted2):
    """
    Takes two sorted lists and compares each of their values, adding the smallest
    value compared to a new list in order to combine them together into one sorted
    list.
    """
    combinedlength = len(sorted1) + len(sorted2)
    combined = []
    count1 = 0       # Keeps track of iteration through first list
    count2 = 0       # Does the same with second list
    while len(combined) < combinedlength:
        if count1 < len(sorted1) and count2 < len(sorted2):
            if sorted1[count1] == sorted2[count2]: # If the two values are equal, add both at the same time
                combined.append(sorted1[count1])
                combined.append(sorted2[count2])
                count1 += 1
                count2 += 1
            elif sorted1[count1] < sorted2[count2]: # Add the smaller value and keep larger where it is
                combined.append(sorted1[count1])
                count1 += 1
            else:
                combined.append(sorted2[count2])
                count2 += 1
        elif count1 == len(sorted1):  # If first list is completelely done, just add the rest in second list
            if count2 < len(sorted2):
                combined.append(sorted2[count2])
                count2 += 1
        else:                         # Reverse case with list 2 completely done
            if count1 < len(sorted1):
                combined.append(sorted1[count1])
                count1 += 1
    return combined

def recursiveMerge(unsorted):
    """
    Takes one unsorted list and recursively splits it in half, merge
    sorting the halves until there is one sorted list.
    """
    unsorted1 = unsorted[0:len(unsorted)//2] # unsorted1 and unsorted2 are the two halves
    unsorted2 = unsorted[len(unsorted)//2:len(unsorted)] 
    if len(unsorted1) == 1 and len(unsorted2) == 1: # merge unsorted lists ONLY when their lengths are 1
        return mergeSort(unsorted1,unsorted2)
    else:
        if len(unsorted1) > 1: # if their length is greater than 1, there's no guarantee they're sorted
            unsorted1 = recursiveMerge(unsorted1) # so put them back through until they're at 1 to ensure merge sort works
        if len(unsorted2) > 1:
            unsorted2 = recursiveMerge(unsorted2)
    merged = mergeSort(unsorted1,unsorted2) # this merge sort can be executed because the two halves are now definitely sorted
    return merged

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

    # Bubble sort's worst case scenario would be a complete reverse order, requring each
    # item to bubble up. The amount they will have to traverse will be shorter each time,
    # but only by 1 index, not enough to break O(n^2), its worst case running time.

    #-------Selection Sort--------#
    # print(selectionSort([5,3,2,4,1]))
    # print(selectionSort([12,98,100,2,9400,45]))
    # print(selectionSort([2,2,2,1,2]))
    # print(selectionSort([2]))

    # Selection sort runs in O(n^2) at worst, as it iterates through all elements in the
    # unsorted list and looks for a maximum, both of which take O(n) time.

    #-------Merge Sort-------#
    # print(mergeSort([1,3,5],[2,4,6]))
    # print(mergeSort([1,50,100],[2,49,70,71,72,73]))
    # print(mergeSort([2],[1]))
    # print(mergeSort([1,2,3],[13,14,15,16]))

    # Merge sort's worst case runs in O(n) time, with n being the length of the combined list.
    # It only compares two values and then appends them to a different list without insertion,
    # all of which is done in constant time. The only linear function is the iteration through
    # each value being added

    #--------Recursive Merge-------#
    # print(recursiveMerge([1,2,3,4,5]))
    # print(recursiveMerge([5,4,3,2,1]))
    # print(recursiveMerge([2, 10, 1, 3, 12, 7]))
    # print(recursiveMerge([1]))

    # Recursive merge's worst case time is O(nlogn), as it recursively cuts the merging in half, and only uses
    # merge sort at worst, which itself runs in O(n) time.

    #-------Benchmarking--------#
    # The fastest function will be merge sort, as it uses two already sorted lists to create
    # one combined sorted list. This pre-existing sorting significantly boosts the time it takes
    # to make one sorted data structure.

    # import time
    # def functionTimer(f, input):
    #     time1 = time.time()
    #     f(input)
    #     time2 = time.time()
    #     return time2 - time1

    # def functionTimer2(f, input1, input2):
    #     time1 = time.time()
    #     f(input1, input2)
    #     time2 = time.time()
    #     return time2 - time1
    
    # print(functionTimer(insertionSort,[6,5,4,3,2,1]) , "Insertion")
    # print(functionTimer(bubbleSort,[6,5,4,3,2,1]) , "Bubble")
    # print(functionTimer(selectionSort,[6,5,4,3,2,1]) , "Selection")
    # print(functionTimer2(mergeSort,[6,5,4],[3,2,1]), "Merge")
    # print(functionTimer(recursiveMerge,[6,5,4,3,2,1]) , "Recursive Merge")

if __name__ == "__main__":
    main()
