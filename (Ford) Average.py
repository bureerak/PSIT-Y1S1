"""Avg by While Loop"""
def main():
    """main function"""
    i = 0
    avg=0
    while i < 10:
        num = int(input())
        avg += num
        i+=1
    print(f"Average is {avg/i}")
main()
