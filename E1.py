import numpy as np
A = [[0,  1,  2,  3],
     [4,  5,  6,  7],
     [8,  9, 10, 11],
     [12, 13, 14, 15]]

np_array = np.array(A)
A_a = np_array[1:3, 1:3]
print('A_a:\n', A_a)
A_b = np_array[:, :-1]
print('A_b:\n', A_b)
A_c = np_array[1:, :]
print('A_c:\n', A_c)

