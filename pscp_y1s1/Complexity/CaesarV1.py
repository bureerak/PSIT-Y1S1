""" CaesarV1 """
def main(shift:int, text:str):
    """ main function """
    temp_out = ''
    for letter in text:
        if letter.isalpha() and letter.isupper():
            temp_out += chr((ord(letter) - 65 + shift) % 26 + 65)
        elif letter.isalpha() and letter.islower():
            temp_out += chr((ord(letter) - 97 + shift) % 26 + 97)
        else:
            temp_out += letter
    print(temp_out)
main(int(input()), input())
