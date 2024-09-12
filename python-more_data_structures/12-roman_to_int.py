#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    if roman_string is not None and not isinstance(roman_string, int):
        i = 0
        while i < len(roman_string):
            if i + 1 != len(roman_string):
                if roman[roman_string[i]] < roman[roman_string[i + 1]]:
                    sub = roman[roman_string[i + 1]] - roman[roman_string[i]]
                    resultado += sub
                    i += 2
                else:
                    resultado += roman[roman_string[i]]
                    i += 1
            else:
                resultado += roman[roman_string[i]]
                i += 1
    return resultado
