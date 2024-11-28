""" Meteorite """
def main():
    """ Meteorite """
    a_meteor = float(input())
    b_broke = int(input())
    c_save = float(input())
    curr_kg = a_meteor
    meteor, count = 1, 0
    while curr_kg>=c_save:
        count+=meteor
        meteor*=b_broke
        curr_kg = a_meteor/meteor
    print(count)
main()
