"""Sonar"""
num = int(input())
ct = num+1
ppp = 0
ggg = num-2
for i in range((num*2)-1):
    if i < num:
        ct=ct-1
    else:
        ct=ct+1
    ct_up = ct+ppp
    ct_low = ct
    ppp+=1
    cp = ct + ggg
    cl = ct+1
    if i>num-1:
        ggg-=1
    for j in range((num*2)-1):
        if i > num-1:
            if (i-(num-1)) <= j and j < (num*2)-(i-(num-2)):
                if cp >= ct:
                    print(f"{cp:>02}",end=" ")
                    cp-=1
                else:
                    print(f"{cl:>02}",end=" ")
                    cl+=1
            else:
                print("  ",end=" ")
        elif i+j >= num-1 and j <= (num-1)+i and i <= num-1:
            if ct_up > ct:
                print(f"{ct_up:>02}",end=" ")
                ct_up-=1
            else:
                print(f"{ct_low:>02}",end=" ")
                ct_low+=1
        else:
            print("  ",end=" ")
    print()

