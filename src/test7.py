def outer(x):
    return  10


def my_func():
    return outer


output_function = my_func()
print(type(output_function))

output = output_function(5)
print(f'Output is {output}')


def get_cuboid_volume(h):
    def volume(l, b):
        return l * b * h

    return volume


volume_height_10 = get_cuboid_volume(10)
cuboid_volume = volume_height_10(5, 4)
print(f'Cuboid(5, 4, 10) volume is {cuboid_volume}')

cuboid_volume = volume_height_10(2, 4)
print(f'Cuboid(2, 4, 10) volume is {cuboid_volume}')



