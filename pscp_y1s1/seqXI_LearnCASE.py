"""Sequence XI"""
def main():
    """main"""
    num = int(input())
    for i in range(-num + 1 , num):
        for j in range(-num + 1 , num):
            if not abs(j) + abs(i) :
                print(f"{str(num):>02}" , end=" ")
            elif abs(j) == num - 1 or abs(i) == num -1:
                print("01" , end=" ")
            else :
                if abs(j) >= abs(i) :
                    print(f"{str(num - abs(j)):>02}" , end=" ")
                else:
                    print(f"{str(num - abs(i)):>02}" , end=" ")
        print()
main()
