"""Docstring"""
def chec(gui,tex,num):
    """no function"""
    if gui in tex:
        print(f"It's Here {num}")

def main():
    """main function"""
    gui = input()
    tex1 = input()
    tex2 = input()
    tex3 = input()
    tex4 = input()
    tex5 = input()
    chec(gui,tex1,1)
    chec(gui,tex2,2)
    chec(gui,tex3,3)
    chec(gui,tex4,4)
    chec(gui,tex5,5)
main()
