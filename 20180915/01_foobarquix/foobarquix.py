from functools import partial

def div_test(factor, text, num):
    return text if num % factor == 0 else ''

def flag_digit(digit, text, num):
    return text if digit == num else ''

div_tests = (
        partial(div_test, 3, 'Foo'),
        partial(div_test, 5, 'Bar'),
        partial(div_test, 7, 'Quix')
        )

flag_digits = (
        partial(flag_digit, 3, 'Foo'),
        partial(flag_digit, 5, 'Bar'),
        partial(flag_digit, 7, 'Quix')
        )

def divisible(num):
    return ''.join(fn(num) for fn in (div_tests))

def is_digit(num):
    return ''.join(fn(num) for fn in (flag_digits))

def foobarquix(num):
    ret = divisible(num) + ''.join(is_digit(int(n)) for n in str(num))
    return ret if ret else str(num)
