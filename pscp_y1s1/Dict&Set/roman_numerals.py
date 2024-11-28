""" ROMAN oiiaioiiiaoiiia """
def main():
    """ main function """
    rome,prev = input(), 'None'
    roman_numerals = {
    'None':float('inf'),
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    temp_out = 0
    for i in rome:
        temp_out += roman_numerals[i]
        if roman_numerals[i] > roman_numerals[prev]:
            temp_out -= roman_numerals[prev]*2
        prev = i
    print(temp_out)
main()
