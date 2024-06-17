"""Temp program"""
def cel(c,type_out):
    """Celsius cal funtion"""
    if type_out == "F":
        c = c*(9/5)+32
    elif type_out == "K":
        c = c+273.15
    elif type_out == "R":
        c = (c+273.15)*(9/5)
    return c
def to_cel(f,type_in):
    """ToCelsius cal"""
    if type_in == "F":
        f = (f-32)*(5/9)
    elif type_in == "K":
        f = f-273.15
    elif type_in == "R":
        f = (f-491.67)*(5/9)
    return f
def main():
    """main program"""
    num = float(input())
    type_in = input()
    type_out = input()
    if type_out == "C":
        print(f"Celsius = {to_cel(num,type_in):.2f}")
    elif type_out == "F":
        num = to_cel(num,type_in)
        print(f"Fahrenheit = {cel(num,type_out):.2f}")
    elif type_out == "K":
        num = to_cel(num,type_in)
        print(f"Kelvin = {cel(num,type_out):.2f}")
    elif type_out == "R":
        num = to_cel(num,type_in)
        print(f"Rankine = {cel(num,type_out):.2f}")
main()
