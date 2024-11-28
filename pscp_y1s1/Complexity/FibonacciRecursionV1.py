""" FibonacciRecursionV1 """
def main(num:int):
    """ main function """
    if not num:
        return 0
    if num == 1:
        return 1
    return main(num - 1) + main(num - 2)
print(main( int(input()) ))
