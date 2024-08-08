""" kayak """
def main():
    """ main function """
    n = int(input())
    info = input().split()
    ans = 0

    for i in range(n*2):
        info[i] = int(info[i])
    info.sort()

    for _ in range(n-1):
        x = info[1]-info[0]
        pos1 = 1
        pos2 = 0
        lenght = len(info)
        for k in range(lenght-1):
            if info[k+1]-info[k]<x:
                x=info[k+1]-info[k]
                pos1 = k+1
                pos2 = k
        ans+=x
        info.remove(info[pos1])
        info.remove(info[pos2])

    print(ans)
main()
