import numpy as np

x = np.array([
    [3, 5, 7, 101],
    [11, 13, 17, 103],
    [23, 27, 31, 105]
])

y = np.array([
    [1234, 2345, 3456, 4567],
    [1357, 3579, 5793, 9357],
    [2468, 4682, 6824, 8246]
])

##############################################################################
##############################################################################
print('\nMathematical Functions')
print(f'sin(x):\n {np.sin(x)}\n')
print(f'cos(x):\n {np.cos(x)}\n')
print(f'tan(x):\n {np.tan(x)}\n')
print(f'2**(x):\n {np.exp2(x)}\n')

##############################################################################
##############################################################################
print('\nAggregate Functions')
print(f'x min: {np.min(x)}')
print(f'x max: {np.max(x)}')
print(f'x mean: {np.mean(x)}')
print(f'x median: {np.median(x)}')
print(f'Standard Deviation: {np.std(x)}\n')

##############################################################################
##############################################################################
print('\nShape Manipulation Functions')
print(f'Initial:\n {x}')
print(f'Reshaped:\n {x.reshape((6, 2))}')
print(f'Reshape & Separate: \n {x.reshape((3, 2, 2))}')

# .flat iterator
for a in x.flat:
    print(a)

print(x.flat[2], '\n')

##############################################################################
##############################################################################
print('\nJoining Arrays')
c = np.concatenate((x, y))
print(c)
print(c.shape, '\n')

c_stack = np.stack((x, y))
print(c_stack)
print(c_stack.shape, '\n')

v_stack = np.vstack((x, y))
print(v_stack)

h_stack = np.hstack((x, y))
print(h_stack)

##############################################################################
##############################################################################
print('\nSplitting Arrays')
print(np.split(v_stack, 3), '\n')
print(np.split(x, 3), '\n')
print(np.vsplit(x, 1), '\n')

##############################################################################
##############################################################################
print('\nAdding Values or Lists to our Arrays')
xyz = [9, 8, 7, 6]

abc = np.append(x, [xyz], axis=0)
# print(abc)

mop = [-2, -3, -5, -7]
qrx = np.insert(abc, 2, mop, axis=1)
print(qrx)




