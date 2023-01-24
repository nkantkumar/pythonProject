def doubler_generator():
    number = 2
    while True:

        number *= number
        yield number

doubler = doubler_generator()
print (next(doubler))


print (next(doubler))


print (next(doubler))


print (type(doubler))