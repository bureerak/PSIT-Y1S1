""" sequence 8 < x < 10 """
def main():
    """ main function """
    x = int( input() )
    for i in range(x):
        space = ""
        for j in range(1, 2 + (2*i)):
            if j > i+1:
                space += f"{ ( i+1 ) + (( i+1 ) - j) :02d} "
            else:
                space += f"{j:02d} "
        print("   " * (x - ( i+1 )), space.strip(), end="", sep="")
        print()
main()
