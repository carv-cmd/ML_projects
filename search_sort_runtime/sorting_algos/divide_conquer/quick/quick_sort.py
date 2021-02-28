# Quick Sort Algorithm

def quick_sorter(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[-1]
        for elem in array:
            if elem < pivot:
                less.append(elem)
            elif elem == pivot:
                equal.append(elem)
            else:
                greater.append(elem)
        less = quick_sorter(less)
        greater = quick_sorter(greater)
        array = less + equal + greater
    return array
