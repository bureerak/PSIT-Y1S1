""" BTU """
def main():
    """ main function """
    room_area = int( input() )
    height = int( input() )
    person = int( input() )
    rtype = input()
    status = input()
    btu = 0
    table = [(2001,34000),(1501,30000),(1401,24000),(1201,23000),\
            (1001,21000),(701,18000),(551,14000),(451,12000),\
            (401,10000),(351,9000),(301,8000),(251,7000),(151,6000),\
            (100,5000)]
    for a, b in table:
        if room_area >= a:
            btu += b
            break
    btu += 0 if person <= 2 else (person - 2)*600
    btu += (height - 8) * 1000 if height>8 else 0
    btu += 4000 if rtype!='Normal' else 0
    btu = btu*1.1 if status == 'facing the sun' else btu*0.9 if status=='shaded' else btu
    print(int(btu))
main()
