"""Docstring"""
def main():
    """main function"""
    pet1 = input()
    pet2 = input()
    pet3 = input()
    pet4 = input()
    pet5 = input()
    width = max(len(pet1),len(pet2),len(pet3),len(pet4),len(pet5)) + 4
    cage(width,pet1)
    cage(width,pet2)
    cage(width,pet3)
    cage(width,pet4)
    cage(width,pet5)
def cage(width,pet):
    """cage building"""
    print("-"*width)
    print(f"|{pet:^{width-2}}|")
    print("-"*width)
main()
