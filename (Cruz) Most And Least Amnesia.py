"""Most Least def function"""
def fmx(num1,num2,num3,num4,num5):
    """max function"""
    if num1 > num2:
        x = num1
    else:
        x = num2
    if num3 > num4:
        y = num3
    else:
        y = num4
    if x > y:
        z = x
    else:
        z = y
    if z > num5:
        return z
    return num5
def fmn(num1,num2,num3,num4,num5):
    """min function"""
    if num1 < num2:
        x = num1
    else:
        x = num2
    if num3 < num4:
        y = num3
    else:
        y = num4
    if x < y:
        z = x
    else:
        z = y
    if z < num5:
        return z
    return num5
def main():
    """main function"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    print(f"Most: {fmx(num1,num2,num3,num4,num5)}, Least: {fmn(num1,num2,num3,num4,num5)}")
main()
