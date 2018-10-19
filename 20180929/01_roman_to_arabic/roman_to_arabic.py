values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

def greater_than(a, b):
    return values[a] > values[b]

def decode_number(text):
    num = []
    for digit in text:
        if not num or digit in num:
            num.append(digit)
        elif greater_than(digit, num[-1]):
            yield (num, digit)
            num = []
        else:
            yield (num, '')
            num = [digit]
    else:
        if num:
            yield (num, '')

def roman_to_arabic(text):
    total = 0

    for (low, high) in decode_number(text):
        partial = values[low[0]] * len(low)
        if high:
            total += values[high] - partial
        else:
            total += partial

    return total
