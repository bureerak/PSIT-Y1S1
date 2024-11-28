""" Divide3Or5 """
def tfsum(num:int):
    """ Divide3Or5 """
    sam = 0
    for i in range(3,num+1):
        if not i%3 or not i%5:
            sam+=i
    print(sam)
tfsum( int(input()) )
