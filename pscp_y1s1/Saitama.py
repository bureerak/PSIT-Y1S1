""" Saitama """
from math import ceil as ce
def main():
    """ main function """
    wid = int( input() )
    sit = int( input() )
    look = int( input() )
    run = int( input() )
    wid_time = int( input() )
    sit_time = int( input() )
    run_time = int( input() )
    look_time = int( input() )
    date = ce(wid/wid_time)
    date = ce(sit/sit_time) if ce(sit/sit_time)>date else date
    date = ce(look/look_time) if ce(look/look_time)>date else date
    date = ce(run/run_time) if ce(run/run_time)>date else date
    print(date)
main()
