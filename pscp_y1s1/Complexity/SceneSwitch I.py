""" SceneSwitch I"""
def main():
    """ main function """
    count, state, iswhite, prev = 0, True, True, None
    while True:
        temp = input()
        if temp == 'End':
            break
        temp = float(temp)
        if not temp:
            continue
        state = not state
        if not state:
            prev = temp
            continue
        if not iswhite:
            iswhite = True
            continue
        if abs(temp - prev)<=6:
            iswhite = False
            count += 1
        else:
            iswhite = True
    print(count)
main()
