# The Merge Sort Algorithm
import random
from datetime import datetime


def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        left_index = right_index = sorted_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                array[sorted_index] = left[left_index]
                left_index += 1
            else:
                array[sorted_index] = right[right_index]
                right_index += 1
            sorted_index += 1

        while left_index < len(left):
            array[sorted_index] = left[left_index]
            left_index += 1
            sorted_index += 1

        while right_index < len(right):
            array[sorted_index] = right[right_index]
            right_index += 1
            sorted_index += 1
    return array


if __name__ == '__main__':
    x = int(input('Enter List Size: '))
    unsorted = [random.randint(1, x**2) for i in range(x)]
    start = datetime.now()
    print(f'\nUnsorted_List: {unsorted}\n')
    print(f'Sorted_List: {merge_sort(unsorted)}')
    print(f'Time to Complete Sort: {datetime.now() - start}')
