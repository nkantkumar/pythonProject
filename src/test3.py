import functools
import operator
regular_list = []

# Transform irregular 2D list into a regular one.
def transform(nested_list):
    for ele in nested_list:
        if type(ele) is list:
            regular_list.append(ele)
        else:
            regular_list.append([ele])
    return regular_list


irregular_list = [[1, 2, [3, 4]], [5, 6, 7], [8, 9, 10], 11]
regular_2D_list = transform(irregular_list)
print('Original list', irregular_list)
print('Transformed list', functools.reduce(operator.iconcat, regular_2D_list, []))