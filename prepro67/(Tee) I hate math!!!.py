"""This math hate program"""
import math
def main():
    """math madness"""
    x_1 = int(input())
    y_2 = int(input())
    ans = (math.log(x_1,2)*3)+(math.cos(math.radians(x_1**2-y_2)))
    ans = (ans / math.sqrt(x_1+y_2)) + math.factorial(y_2)
    print(f"{ans:.2f}")
main()
