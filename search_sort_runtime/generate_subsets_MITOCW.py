# Generates all possible subsets given list
################################################################
################################################################
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


################################################################
################################################################
gen_sub = gen_subsets([1, 2, 3, 4])
print(gen_sub)
print(len(gen_sub) - 1)
