# A simple yet highly inefficient Bubble Sort Algorithm
# Runtime Complexity Big-O(n^n) for complete list sort
import random
from datetime import datetime


def test(size):
    """
    Generates a random list of integers, then bubble sorts said list
    Prints total_time to complete process
    :param size: random_list size to be generated for sorting
    :return: sorted list
    """
    start = datetime.now()

    def bubble_sort(unsorted):
        """
        Sorts single largest element to end of list
        Function called in a loop to sort entire list
        Inner loop: only loops over unsorted[:-(i+1)], ignores sorted els at end in each new iter
        :param unsorted: random generated list
        :return: list with one element sorted to correct position
        """
        for i in range(len(unsorted)):  # n_times
            for k in range(len(unsorted) - i - 1):  # n-i_times
                if unsorted[i] > unsorted[i + 1]:  # 1_PrimitiveOp
                    unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]  # 1_PrimitiveOp
                    break
                else:  # 1_PrimitiveOp
                    break
        return unsorted  # 1_PrimitiveOp

    quickie = [random.randint(1, size*2) for rands in range(size)]
    print(f'Unsorted_List:\n{quickie}\n')

    for each in range(len(quickie)):  # n_times
        bubble_sort(quickie)  # n^2-n

    print(f'\nTime To Complete Bubble Sort: {datetime.now() - start}\n')
    print(f'Sorted_List:\n{quickie}')


if __name__ == '__main__':
    user_input = int(input("Length of Random List: "))
    test(user_input)
