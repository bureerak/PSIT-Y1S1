"""Docstring"""
def main():
    """main function"""
    mood = input()
    mes = input()
    if mood == "Tired":
        print(f"\"{mes}\"")
        print("(=_=)")
    elif mood == "Sad":
        print(f">>\'{mes}\'<<")
        print("\\ToT/")
    elif mood == "Happy":
        print(f"\\\\\"{mes}\"//")
        print("(^o^)")
    elif mood == "Angry":
        print(f"!!!\'{mes}\'!!!")
        print("(*O_O*)")
    elif mood == "Shy":
        print(f"<\"\'{mes}\'\">")
        print("(^///^)")
    else:
        print("\\\'?\'/")
main()
