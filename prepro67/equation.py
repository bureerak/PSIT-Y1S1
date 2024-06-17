"""Equation Program"""
def main():
    """calculate function"""
    num_x = input()
    num_y = input()
    num_x = float(num_x)
    num_y = float(num_y)
    ans = ((num_x+3)*2*num_y)**2-(num_x*num_y+4)
    ans /= (2*num_x+3*num_y)
    ans += (num_x*num_y)**2
    print(f"{ans:.3f}")
main()
