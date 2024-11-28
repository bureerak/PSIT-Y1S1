""" Bonus """
def main():
    """ main function """
    salary = int(input())
    year = int(input())
    month = int(input())
    if month>=10:
        year+=1
    year = min(year,20)
    get = year*salary
    if get > 1000000:
        get=1000000
    if get < 5000:
        get=5000
    print(get)
main()
