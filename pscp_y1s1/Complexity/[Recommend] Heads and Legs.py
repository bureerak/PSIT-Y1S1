""" HeadnLegs """
def findanimal(a:int, b:int):
    """ a = animal | b = legs  """
    least = a * 2
    b -= least
    print('Impossible' if b<0 or a-(b//2)<0 or b%2 else f"{(b//2)} {a-(b//2)}")
findanimal( int(input()), int(input()) )
