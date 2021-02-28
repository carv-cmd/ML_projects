# Insertion Sort Algorithm  ** [Big-O(n**2)] Runtime Complexity **
import random


def insertion_sort(unsorted):
    """
    Splits list into 2 'sorted' and 'unsorted' sublist
    For loop starts at 1, i.e. the 0 index of the 'unsorted' sublist
    Leaving a 'sorted' sublist of 1 element to the left
    With each iteration unsort_sublist shrinks and sorted_sublist grows
    Left sublist is always sorted, therefore, unsort_sublist[0] or ('list[j]') is the element we move
    If while conditional is true, j_val will be assigned j-1_val and checked against the rest of sub_sorts elements
    Check notes.txt on this project for additional information about this code
    """
    for i in range(1, len(unsorted)):
        val = unsorted[i]
        j = i
        while j > 0 and unsorted[j-1] > val:
            unsorted[j] = unsorted[j-1]
            j = j - 1
        unsorted[j] = val
    return unsorted


# size = int(input('Enter Random List Length: '))
size = 100000
unsorted_list = [random.randint(1, size**2) for randy in range(1, size)]
print(f'\nUnsorted_List:\n{unsorted_list}')

sorted_list = insertion_sort(unsorted_list)
print(f"\nSorted_List:\n{sorted_list}")
print(f'\nSorted_List is Initial_List == {sorted_list is unsorted_list}')
