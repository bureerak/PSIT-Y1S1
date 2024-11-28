""" Niwan """
import math
def xn_func(n):
    """ x """
    x_num = math.log2(n**2)
    x_num /= 2*n*math.log2(n)
    x_num += 2
    return x_num
def yn_func(n,s):
    """ y """
    y_num = math.sin(math.radians(30))+(2*s)**0.5
    y_num /= xn_func(n)+3
    return y_num
def zn_func(k):
    """ z """
    z_num = 8456 * (xn_func(k))**4
    z_num /= 24*k
    z_num += (yn_func(k,k))**2
    return z_num
def main():
    """ main function """
    num_n = float(input())
    num_s = float(input())
    num_k = float(input())
    xxx = xn_func(num_n)
    yyy = yn_func(num_n,num_s)
    zzz = zn_func(num_k)
    print(f"X: {xxx:.1f}",f"Y: {yyy:.1f}",f"Z: {zzz:.1f}",sep=", ")
main()
