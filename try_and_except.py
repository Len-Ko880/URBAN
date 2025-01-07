def add_everything_up(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        if type(a) == int or isinstance(a, float) and type(b) == str:
            result = str(a) + b
        elif type(a) == str and isinstance(b, int) or isinstance(b, float):
            result = a + str(b)
    return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

