"""Missing Docstring"""
import math
def main():
    """main function"""
    a_1 = float(input())
    b_2 = float(input())
    degree_c = float(input())
    if degree_c < 180:
        c_3 = a_1**2 + b_2**2 - 2*a_1*b_2*math.cos(math.radians(degree_c))
        c_3 = round(c_3**0.5,2)
        area = 0.5*a_1*b_2*math.sin(math.radians(degree_c))
        area = round(area,2)
        print(f"{c_3:.2f}")
        print(f"{area:.2f}")
    else:
        print("Not a Triangle")
main()
