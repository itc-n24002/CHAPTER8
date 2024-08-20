functions = [sum, min, max]

numbers = range(1, 11)
list(numbers)

functions = [sum, min, max]
number_list = range(1, 11)
for func in functions:
    print("Functon: {}, Result: {}".format(func.__name__, func(number_list)))
