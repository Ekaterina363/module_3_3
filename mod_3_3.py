
def print_params(a = 1, b ="строка", c = True):
    print(a, b, c)

print_params()
print_params(b = 25)

print_params(c=[1, 2, 3])

values_list = [5, 0.3, "element"]
print_params(*values_list)

values_dict = {"a":4, "b":2.56, "c":False}
print_params(**values_dict)

values_list_2 = [8, "восемь"]
print_params(*values_list_2, 42)

