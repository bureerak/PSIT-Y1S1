"""Docstring"""
def main():
    """SoS"""
    num = ""
    i=1
    num1 = 0
    num2 = 0
    num3 = 0
    while num!="End":
        num = input()
        if num == "End":
            break
        num = int(num)
        if num < num1 or i == 1:
            num3 = num2
            num2 = num1
            num1 = num
        elif num < num2 or i == 2:
            num3 = num2
            num2 = num
        elif num < num3 or i == 3:
            num3 = num
        i+=1
    print(f"The Third is {num3}")
main()
