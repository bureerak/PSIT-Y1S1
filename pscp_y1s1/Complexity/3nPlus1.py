""" 3nPlus1 """
def tilone(num:int, count = 0):
    """ do sth to make it 1 """
    if num == 1:
        return count
    if not num%2:
        num= num//2
    else:
        num=(num*3)+1
    return tilone(num, count+1)
def main():
    """ input here """
    while True:
        com = int(input())
        if not com:
            break
        print(tilone(com) + 1)
main()
