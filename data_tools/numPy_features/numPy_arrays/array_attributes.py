import numpy as np

a = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [10, 20, 30],
        [40, 50, 60]
    ]
], dtype=float)

print(f'Array Shape: {a.shape}')
print(f'Array Size: {a.size}')
print(f'Array Dimensions: {a.ndim}')
print(f'Array Datatype: {a.dtype}')

print(a)
