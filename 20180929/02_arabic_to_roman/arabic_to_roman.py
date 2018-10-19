
mapping = (
        (1000, 'M', 'M'),
         (900, 'CM', None),
         (500, 'D', 'C'),
         (400, 'CD', None),
         (100, 'C', 'C'),
          (90, 'XC', None),
          (50, 'L', 'X'),
          (40, 'XL', None),
          (10, 'X', 'X'),
           (9, 'IX', None),
           (5, 'V', 'I'),
           (4, 'IV', None),
           (1, 'I', 'I'),
)


def arabic_to_roman(number):
    text = ''

    for num, letter, repeat in mapping:
        if number >= num:
            times = number // num
            if times == 1:
                text += letter
            else:
                text += letter + repeat * (times - 1)
            number -= num * times

    return text
