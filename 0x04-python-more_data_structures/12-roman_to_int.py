#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_numbers = {'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    if not roman_string or type(roman_string) != str:
        return 0
    for k in range(len(roman_string)):
        if k > 0 and rom_numbers[roman_string[k]] > rom_numbers[roman_string[k - 1]]:
            sum += rom_numbers[roman_string[k]] - 2 * \
                rom_numbers[roman_string[k - 1]]
        else:
            sum += rom_numbers[roman_string[k]]
    return sum
