def add_everything_up(a, b):
    try:

        if isinstance((int, float), a) and isinstance((int, float), b):
            return a + b

        elif isinstance(str, a) and isinstance(str, b):
            return a + b

        else:
            raise TypeError


    except TypeError:

        return f'{str(a)}{str(b)}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
