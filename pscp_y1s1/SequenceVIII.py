""" SequenceVII """
def main():
    """ main funtion """
    x = int( input() )
    for i in range(x):
        space = ""
        print( "   " * (x-(i+1)), end="" )
        for j in range(1, i+2):
            space += f"{j:02d} "
        print( space.strip(), end="" )
        print()
main()
