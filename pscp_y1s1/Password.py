""" def main """
import math
def main():
    """ main function """
    key = input()
    lenght,pool = len(key),0
    lower,upper,num,special = False,False,False,False
    for i in key:
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
        if i.isnumeric():
            num = True
        if not i.isalnum():
            special = True
    pool+=26 if lower else 0
    pool+=26 if upper else 0
    pool+=10 if num else 0
    pool+=32 if special else 0
    bit = int(math.log(pool**lenght,2))
    print(bit)
    if bit < 28:
        print("Very Weak")
    elif bit < 36:
        print("Weak")
    elif bit < 60:
        print("Reasonable")
    elif bit < 128:
        print("Strong")
    else:
        print("Very Strong")
main()
