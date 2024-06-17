"""arithmetic"""
def main():
    """main function"""
    type_arith = input()
    num = int(input())
    start = int(input())
    times = int(input())
    if type_arith == "d":
        for _ in range(times):
            print(f"[{start:^{len(str(start))+2}}]",end="")
            start += num
    elif type_arith == "r":
        for _ in range(times):
            print(f"[{start:^{len(str(start))+2}}]",end="")
            start *= num
main()
