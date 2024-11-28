""" MusicLove """
def main(num):
    """ main function """
    sth = {}
    for _ in range(num):
        temp = input().split('-')
        sth[temp[0]] = sth.get(temp[0], [])
        sth[temp[0]].append(temp[1].strip())
    for i, j in sth.items():
        print(i, *j, sep="\n")
main( int(input()) )
