def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(8, False)
print_params(4)
print_params(6, 'hello', None)

print_params(b = 25) #работает
print_params(c = [1, 2, 3]) #работает

values_list = [22, 'cat', False]
values_dict = {'a' : 18, 'b' : 'dog', 'c' : None}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [38, 'paper']
print_params(*values_list_2, 42) #работает