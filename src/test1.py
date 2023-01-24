import numpy as np

nums = np.array([1, 2, 3, 4, 5])

for num in nums:
    print(num)
list1 = [1, 2, (4, 5, 6), 3, 4, 5, 6]

fruits = ["Apple", "Mango", "Banana", "Peach"]


lst1 = [1, 2, 3, 4, 5]

lst1 = list(map(lambda v: v ** 2, lst1))

print(lst1)


import sys

a_list = list()
a_tuple = tuple()

a_list = [1,2,3,4,5]
a_tuple = (1,2,3,4,5)

print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))

