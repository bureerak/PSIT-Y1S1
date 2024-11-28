""" CeasarV2 """
def main(text):
    """ CaesarV2 """
    sep1, cheker = '', ["what", "when", "why", "which", "this", "there",\
    "where", "the", "is", "am", "are", "you", "we", "they", "he", "she", "it"]
    sep2 = " "
    text = list(map(caesar,text))
    text = sep1.join(text)
    text = text.split()
    for i in text:
        if i in cheker:
            return text
    return main(sep2.join(text))

def caesar(code):
    """ Decode """
    if not code.isalpha():
        return code
    if code.isupper():
        code = chr((ord(code) - 65 + 1) % 26 + 65)
    elif code.islower():
        code = chr((ord(code) - 97 + 1) % 26 + 97)
    return code
print(*main( input() ))
