# Selection Sort
# Yet another simple, but Quadratic Runtime Complexity
import random


def selection_sorter():
    """
    Outer function requests list size from user
    Generates list of n length containing random integers from 1 to n**2
    Passes list to selection sort and returns sorted list
    """
    def selection_sort(pls_sort):
        """
        Outer loop 'i' is subset[-1] index, or the 'smallest starting element' in each iteration
        For each outer loop iter, inner loop iterations equate to: "pls_sort[i:]"
        Inner compares each element after 'i' with min_val locating smallest el in unsorted subset
        After len(subset)_iters, element[i] and element[min_val] are swapped
        Since its searching for 'smaller than min_val' not '<=' this handles the case of duplicates
        :param: pls_sort list is the random generated list of n length
        :returns: sorted list to selection_sorter function
        """
        print(f'\nInitial List:\n{pls_sort}')
        for i in range(len(pls_sort)):
            min_val = pls_sort[i]
            min_index = i
            for num in range(i, len(pls_sort)):
                if pls_sort[num] < min_val:
                    min_val = pls_sort[num]
                    min_index = num
            pls_sort[i], pls_sort[min_index] = pls_sort[min_index], pls_sort[i]
        return pls_sort
    size = int(input('Size of Random Generated List: '))
    return selection_sort([random.randint(1, size**2) for randy in range(1, size)])


print(f'\nSorted List:\n{selection_sorter()}')
