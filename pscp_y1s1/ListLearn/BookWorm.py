""" Book Worm """
def book(num):
    """ Book """
    for _ in range(num):
        time = float( input() )
        books = int( input() )
        to_read = [ float( input() ) for _ in range(books)]
        to_read.sort()
        x, y = 0, 0
        for i in to_read:
            if x + i <= time:
                x, y = x + i, y + 1
        print(y)
book( int(input()) )
