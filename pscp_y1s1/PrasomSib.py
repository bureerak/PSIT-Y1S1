"""PrasomSib problem via iJudge during pair programming"""
def tilten():
    """
    This function finds maximum amount possible to add number until 10.
    Arguments:
    - num (str): Long line of number to find

    Returns:
    - count (int): Amount of possible count.

    Raises:
       None.
    """
    num = input()
    length = len(num)
    count = 0
    temp = 0
    for i in range(length):
        temp += int(num[i])
        for j in range(i+1,length):
            temp += int(num[j])
            if temp==10:
                count+=1
                break
            if temp>10:
                break
        temp = 0
    print(count)
tilten()
