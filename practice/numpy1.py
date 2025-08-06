import numpy as np

# a = np.array([10, 20, 30])
# b = np.array([[10, 20, 30], [40, 50, 60]])
# c = np.array([[[10, 20, 30], [40, 50, 60]], [[10, 20, 30], [40, 50, 60]]])



# print(a.shape)
# print(b.shape)
# print(c.shape)

# import numpy as np

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])

# print(a.ndim)        # 2         → Number of dimensions
# print(a.shape)       # (2, 3)    → Tuple of array dimensions
# print(a.size)        # 6         → Total number of elements
# print(a.dtype)       # int64     → Data type of elements (may be int32 on 32-bit)
# print(a.itemsize)    # 8         → Bytes per element (8 for int64, 4 for int32)
# print(a.nbytes)      # 48        → Total bytes = size * itemsize (6 * 8)
# print(a.T)           # [[1 4] [2 5] [3 6]] → Transpose (rows become columns)
# print(list(a.flat))  # [1, 2, 3, 4, 5, 6] (as np.int64) → Flat iterator values

# b = a.reshape(3, 2)
# print(b)             # [[1 2] [3 4] [5 6]] → Reshaped to 3x2

# c = a.ravel()
# print(c)             # [1 2 3 4 5 6] → Returns flattened 1D copy

# d = a.flatten()
# print(d)             # [1 2 3 4 5 6] → Similar to ravel, but always a copy

# e = a.copy()
# print(np.shares_memory(a, e))    # False → e is a deep copy

# print(np.sum(a))          # 21      → Sum of all elements
# print(np.mean(a))         # 3.5     → Mean of all elements
# print(np.std(a))          # 1.7078  → Standard deviation
# print(np.min(a))          # 1       → Minimum value
# print(np.max(a))          # 6       → Maximum value
# print(np.cumsum(a))       # [1 3 6 10 15 21] → Cumulative sum
# print(np.prod(a))         # 720     → Product of all elements

# print(np.sum(a, axis=0))  # [5 7 9]     → Sum down each column
# print(np.sum(a, axis=1))  # [6 15]      → Sum across each row

# print(a[0])          # [1 2 3]     → First row
# print(a[:, 1])       # [2 5]       → Second column
# print(a[1, 2])       # 6           → Element at row 1, column 2

# print(np.sort(a))        # [[1 2 3] [4 5 6]] → Row-wise sort
# print(np.argsort(a[1]))  # [0 1 2]          → Indices that would sort row 1
# print(np.where(a > 3))   # (array([1, 1, 1]), array([0, 1, 2])) → Positions > 3
# print(np.argmax(a))      # 5               → Index of max value in flattened array
# print(np.argmin(a))      # 0               → Index of min value in flattened array

# print(a > 3)             # [[False False False] [ True  True  True]]
# print(np.any(a > 5))     # True          → Is any element > 5?
# print(np.all(a < 10))    # True          → Are all elements < 10?

# f = a.astype(float)
# print(f)                 # [[1. 2. 3.] [4. 5. 6.]] → Elements converted to float


# a = np.zeros((2, 3))
# print(a)  # [[0. 0. 0.] [0. 0. 0.]]

# b = np.ones((3, 2), dtype=int)
# print(b)  # [[1 1] [1 1] [1 1]]

# c = np.full((2, 2), 7)
# print(c)  # [[7 7] [7 7]]

# d = np.eye(3)
# print(d)  # [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]]

# e = np.arange(1, 10, 2)
# print(e)  # [1 3 5 7 9]

# f = np.linspace(0, 1, 5)
# print(f)  # [0.   0.25 0.5  0.75 1.  ]

# g = np.random.rand(2, 3)
# print(g)  # Random floats between 0 and 1 (e.g. [[0.62 0.42 0.58] [0.96 0.12 0.15]])

# h = np.random.randint(10, 20, size=(2, 2))
# print(h)  # Random ints like [[14 11] [13 19]]


# a = np.array([[1, 2, 3],
#               [4, 5, 6]])

# b = np.array([10, 20, 30])
# print(a + b)  
# # [[11 22 33]
# #  [14 25 36]]
# # b (1D) is broadcasted to each row of a

# a = np.array([10, 15, 20, 25, 30])
# mask = a > 20
# print(mask)         # [False False False  True  True]
# print(a[mask])      # [25 30] → Only values > 20

# # Directly in one line
# print(a[a % 10 == 0])  # [10 20 30]

# a = np.array([10, 20, 30, 40, 50])
# indices = [1, 3, 4]
# print(a[indices])   # [20 40 50]

# # 2D example
# b = np.array([[1, 2],
#               [3, 4],
#               [5, 6]])

# row_idx = [0, 1, 2]
# col_idx = [1, 0, 1]
# print(b[row_idx, col_idx])  # [2 3 6] → Picks (0,1), (1,0), (2,1)

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])

# print(a)

# a[0] = [7,8,9]
# print(a)

# [[7 8 9]
#  [4 5 6]]

# a[0][1] = 0
# print(a)

# [[7 0 9]
#  [4 5 6]]

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a[0][2]) 
print(a[0, 2]) 
