"""Docsting"""
def main():
    """Main function"""
    days = int(input())
    ans_day = days
    ans = ["Tuesday","Wednesday","Thursday",
           "Friday","Saturday","Sunday","Monday"]
    if days > 6 :
        days = days%7
    print(f"{ans_day:,} days from today will be {ans[days]}!")
main()
