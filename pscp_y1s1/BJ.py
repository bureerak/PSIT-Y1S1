""" BJ ย่อมาจาก Black Jack จริงๆนะ """
def main():
    """ main function """
    num = int( input() )
    a_count = 0
    score = 0
    for _ in range(num):
        card = input()
        if card in ("J","Q","K"):
            score += 10
        elif card == "A":
            score += 11
            a_count += 1
        else:
            score += int(card)
    while score > 21 and a_count:
        score-=10
    print(score)
main()
