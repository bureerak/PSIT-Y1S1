""" Salary """
def salary(day,total_h=0):
    """ return salary in 1 month """
    if day:
        x, day = float(input()), day-1
        total_h += int(x)+1 if x > int(x) else int(x)
        salary(day,total_h)
    else:
        print(8720*total_h)
salary(int(input()))
