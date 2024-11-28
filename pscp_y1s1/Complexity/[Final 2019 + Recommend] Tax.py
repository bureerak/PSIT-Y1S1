""" Practice """
def main(year, cxc):
    """ main function """
    sal = 0
    remain = cxc
    if not cxc:
        print(f"{0:.2f}")
        return
    for i, j in ( (600, 0.50),(1200, 1.50),(float('inf'), 4) ):
        sal += min(remain,i) * j
        remain -= min(remain,i)
    for i,j in ( (9,0.6), (8,0.7), (7,0.8), (6,0.9) ):
        if year == i:
            sal *= j
            break
    if year >= 10:
        sal *= 0.5
    print(f"{sal:.2f}")
main( int( input() ), int( input() ) )
