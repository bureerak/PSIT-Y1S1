""" DebaRoad  """
def main(num:int):
    """ main function """
    if 0 <= num <= 5.032:
        print("Bangkok")
    elif 5.032 < num <= 35.477:
        print('Samut Prakarn')
    elif 35.477 < num <= 52.900:
        print('Chachoengsao')
    elif 52.900 < num <= 58.855:
        print('Chon Buri')
    else:
        print('InValid')
main(float(input()))
