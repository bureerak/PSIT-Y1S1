""" bill week 4 """
def main():
    """ main function """
    bill = int(input())
    service = bill * 0.1
    if service < 50:
        bill += 50
    elif service > 1000:
        bill += 1000
    else:
        bill+=service
    print(f"{bill*1.07:.2f}")
main()
