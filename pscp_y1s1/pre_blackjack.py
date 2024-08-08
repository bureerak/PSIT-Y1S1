"""a"""
def score(a,score1,score2,score3=0):
    """score function"""
    ans = 0
    if score1 not in ("J","Q","K","A"):
        score1 = int(score1)
        ans += score1
    elif score1 in ("J","Q","K"):
        ans += 10

    if score2 not in ("J","Q","K","A"):
        score2 = int(score2)
        ans += score2
    elif score2 in ("J","Q","K"):
        ans += 10

    if score3 not in ("J","Q","K","A"):
        score3 = int(score3)
        ans += score3
    elif score3 in ("J","Q","K"):
        ans += 10

    for _ in range(a):
        if ans+11<=21:
            ans+=11
        else:
            ans+=1
    if a > 1 and ans>21:
        ans-=10
    return ans

def main():
    """main function"""
    num = int(input())
    cur_score = 0
    a_count = 0
    if num == 2:
        fst = input()
        sec = input()
        if fst == "A":
            a_count +=1
        if sec == "A":
            a_count +=1
        cur_score = score(a_count,fst,sec)
    elif num == 3:
        fst = input()
        sec = input()
        trd = input()
        if fst == "A":
            a_count +=1
        if sec == "A":
            a_count +=1
        if trd == "A":
            a_count +=1
        cur_score = score(a_count,fst,sec,trd)
    print(cur_score)
main()
