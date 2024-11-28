def main(time, count = 0, fst = 0, sec = 1):
    if time <= 0:
        return
    if count == 0:
        print(fst,end=" ")
        count+=1
        time-=1
        main(time, count, fst, sec)
    elif count == 1:
        print(sec,end=" ")
        count+=1
        time-=1
        main(time, count, 0, 1)
    elif time:
        time-=1
        print(fst+sec,end=" ")
        fst, sec = sec, fst+sec
        main(time, count, fst, sec)
main(int( input() ))
