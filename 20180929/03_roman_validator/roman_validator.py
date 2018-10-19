import re

pattern = r"""M{0,3}                 # Maybe 1000-3000
          (?:CM|DC{0,3}|CD|C{0,3})?  # Maybe (900 or 500-800 or 400 or 100-300)
          (?:XC|LX{0,3}|XL|X{0,3})?  # Maybe (90 or 50-80 or 40 or 10-30)
          (?:IX|VI{0,3}|IV|I{0,3})?  # Maybe (9 or 5-8 or 4 or 1-3)
              """
def roman_validator(text):
    if not text:
        return False
    Return re.match("^" + pattern + "$", text, re.X) is not None
