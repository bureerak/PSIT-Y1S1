"""Docstring"""
def function_x(x):
    """Function(X)"""
    x = 3*x + 5
    return x
def function_g(x):
    """function(G)"""
    x = (function_x(4*x)+23) / 2
    return x
def function_h(x,y):
    """function(H)"""
    h = (function_g(function_x(3*y)+2*x)-function_g(2*y)) * (function_x(4*y)+5*x)
    return h
def main():
    """this is main"""
    num_x = float(input())
    num_y = float(input())
    ans = function_h(num_x,num_y)
    print(f"{ans:.2f}")
main()
