""" Day2011 """
def whatday(date, month):
    """ return day by date """
    day_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = {
        '0':'Friday','1':'Saturday','2':'Sunday',\
        '3':'Monday','4':'Tuesday','5':'Wednesday',\
        '6':'Thursday'
        }
    day_of_year = sum(day_of_month[:month-1]) + date
    print(day[str(day_of_year % 7)])
whatday(int(input()), int(input()))
