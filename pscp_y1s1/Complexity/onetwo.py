""" OneTwo """
def main(num:int):
    """ main function """
    if num == 1:
        return '1'
    if num == 2:
        return '2'
    return main(num - 1) + main(num - 2)
print(main( int(input()) ))
