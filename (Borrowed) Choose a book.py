"""Docstring Easy"""
import math
def main():
    """main function"""
    num_n = int(input())
    num_r = int(input())
    ans = math.factorial(num_n) / (math.factorial(num_r) * math.factorial(num_n-num_r))
    print(int(ans))
main()
