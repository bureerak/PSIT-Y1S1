""" palindome """
def main():
    """ main function """
    time = int(input())
    curr = input()
    fst = curr[:curr.find(":")]
    sec_one = curr[curr.find(":")+1]
    sec_two = curr[curr.find(":")+2]
    i = 1
    while i <= time:
        if len(fst) == 1:
            sec_one = sec_one if int(sec_two) < int(fst) else (1+int(sec_one))
            if int(sec_one)>5:
                fst=str(int(fst)+1)
                sec_one, sec_two = 0,0
                continue
            sec_two = fst
            print(f"{fst}:{sec_one}{sec_two}")

        if len(fst) == 2:
            fst = fst if int(sec_two) < int(fst[0]) else str(int(fst)+1)
            if int(fst)>23:
                fst = str(int(fst)%24)
                sec_one, sec_two = 0,0
                print(f"{fst}:00")
                i+=1
                continue
            if int(fst[1])>5:
                fst=str(int(fst)+1)
                continue
            sec_one,sec_two = fst[1],fst[0]
            print(f"{fst}:{sec_one}{sec_two}")
        i+=1
main()
