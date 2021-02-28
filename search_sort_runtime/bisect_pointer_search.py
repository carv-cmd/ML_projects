# Bisection Search in n*log(n) runtime
# Passes Pointers for 'high' and 'low' instead of list subscription
# Returns element index position in sorted list

###############################################################################
###############################################################################
import random
from quick_sort import quick_sorter as quick


###############################################################################
###############################################################################
def bisection(array, sv):
    def bisect(a, sva, low=0, high=len(array)-1):
        if low == high:
            return False
        else:
            mid = (low + high) // 2
            if sva == a[mid]:
                return mid
            elif sva > a[mid]:
                low, mid = mid+1, low
            else:
                high, mid = mid, high

        return bisect(a, sva, low, high)
    return bisect(array, sv)


###############################################################################
###############################################################################
x = 500
unsorted = [random.randint(1, x*100) for i in range(x)]
rand_sorted = quick(unsorted)
print(f'\nSorted List to Perform a Bisection Search On:\n{rand_sorted}'
      f'\n--------------------------------------------------------------\n')

item = int(input("Enter a Number to Check for: "))

bs = bisection(rand_sorted, item)
if bs is not False:
    print(f'\nFound:({item}) @ rand_sorted[{bs}] == {rand_sorted[bs]}')
else:
    print(f'\nItem({item}) NOT IN Array..')
