# Generates all possible subsets of a given list
# Recursively builds these permutations
# Credit to MIT Professor (get_name) for this fascinating piece of code


def gen_subsets(k):
    """
    :param: list 'k' passed into function
    :returns: list w/ lists of all possible subsets from k
    """
    if len(k) == 0:
        return [[]]
    smaller = gen_subsets(k[:-1])

    extra = k[-1:]
    new = []

    for small in smaller:
        new.append(small + extra)
    return smaller + new


super_list = [1, 2, 3, 4]
gen_sub = gen_subsets(super_list)
print(f'\nSubsets of {super_list}'
      f'\n---------------------------\n{gen_sub}')
print(f'\nNumber of Subsets: {len(gen_sub) - 1}')
