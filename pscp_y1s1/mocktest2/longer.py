""" Longer """
import math
def main():
    """ main function """
    r_in = float(input())
    a_in = float(input())
    b_in = float(input())
    cir = 2*math.pi*r_in
    rec = a_in*2 + b_in*2
    if cir > rec:
        print("Circle is longer")
    elif rec > cir:
        print("Rectangle is longer")
    else:
        print("Equal")
    print(f"{abs(cir-rec):.5f}")
main()
