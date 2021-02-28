# Bisection Search Algorithm. Otherwise known as binary search
# Duplicates list, not truly log(n) runtime
import random
from quick_sort import quick_sorter as quick


def bisection(array, search):
    mid = len(array) // 2
    print(f'\nBisected Array:\n{array}')
    if len(array) == 1 and search != array[mid]:
        return False
    elif search == array[mid]:
        return True
    elif search > array[mid]:
        return bisection(array[mid+1:], search)
    else:
        return bisection(array[:mid], search)


# x = int(input('\nEnter a Random List Size to be Generated: '))
x = 100
unsorted = [random.randint(1, x*100) for i in range(x)]

print(f'\nUnsorted Initial List:\n{unsorted}')

rand_sorted = quick(unsorted)
print(f'\nSorted List to Perform a Bisection Search On:\n{rand_sorted}'
      f'\n--------------------------------------------------------------\n')

item = int(input("Enter a Number to Check for: "))

if bisection(rand_sorted, item) is False:
    print(f'{item} is NOT Present in Array')
else:
    print(f'\nFound {item} in array')
