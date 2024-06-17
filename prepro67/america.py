"""doc"""
def parent(numer):
    """parent interstate"""
    lenght = len(numer)
    if lenght>=2:
        #สามหลักกับสองหลัก
        if numer[-1] in ("0","5"):
            if numer[-2] == "0":
                print(f"I-{numer[-1]}")
            else:
                print(f"I-{numer[-2:]}")
    elif numer[-1] == "5":
        #หลักเดียวเป็น 5 เท่านั้น
        print(f"I-{numer[-1]}")

def main():
    """main function"""
    num = int(input())
    num = str(num)
    lenght = len(num)
    if 0 < lenght < 3:
        if lenght == 1 and num[-1] == "0":
            #ดักเลขศูนย์ตัวเดียว
            print("Others")
        elif num[-1] == "0":
            print("Horizontal Major Interstate")
            parent(num)
        elif num[-1] == "5":
            print("Vertical Major Interstate")
            parent(num)
        else:
            print("Others")
    elif lenght == 3 and num[-1] in ("0","5"):
        if not int(num[0])%2 and 5<=int(num[-2:])<=95:
            print("Even Minor Interstate")
            parent(num)
        elif int(num[0])%2 and 5<=int(num[-2:])<=95:
            print("Odd Minor Interstate")
            parent(num)
        else:
            print("Others")
    else:
        print("Others")
main()
