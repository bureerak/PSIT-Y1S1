""" PH """
def phfind():
    """ PH 0-14 """
    text = float( input() )
    if text == 7:
        print('neutral')
    elif 0 <= text < 7:
        print('acidic')
    elif 7 < text <= 14:
        print('akaline')
    else:
        print('error')
phfind()
