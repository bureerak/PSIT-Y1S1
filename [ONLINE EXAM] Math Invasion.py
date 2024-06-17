"""Docstring"""
import math

def ffunc(x):
    """f function"""
    x = 7*(x**2) + 3*x + 11
    return x
def gfunc(x,y):
    """g function"""
    res = (math.sqrt(3*ffunc(x)) / (4*y)) - 5*x*y
    return res
def hfunc(x,y,z):
    """h function"""
    res = gfunc(ffunc(z**2)+(x**y),gfunc(x*y,ffunc(gfunc(y,math.sqrt(z**5)))))
    res = res / (((2*x)*math.sqrt(z*(y**2)))+91)
    res = res + ((7*x*y)/(13*z)) + 6
    return res

def main():
    """main function"""
    num_x = float(input())
    num_y = float(input())
    num_z = float(input())
    print(f"{round(hfunc(num_x,num_y,num_z),3):.3f}")
    print(f"{round(gfunc(num_x,num_y),3):.3f}")
    print(f"{round(ffunc(num_x),3):.3f}")
main()
