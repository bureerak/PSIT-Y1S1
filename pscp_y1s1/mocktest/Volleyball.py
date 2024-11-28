""" Volley Ball """
def main(text):
    """ main function """
    score_a, score_b, g_set = 0, 0, 1
    awin, bwin, end = 0, 0, False

    for i in text:
        crite = 15 if g_set == 5 else 25

        if i == "A":
            score_a+=1
        elif i == "B":
            score_b+=1

        check1 = bool(score_a >= crite and score_a - score_b >= 2)
        check2 = bool(score_b >= crite and score_b - score_a >= 2)
        if check1 or check2:
            print(f"Set {g_set}: A ({score_a}) | B ({score_b})")
            g_set+=1
            score_a, score_b = 0, 0
            awin+= 1 if check1 else 0
            bwin+= 1 if check2 else 0
        if end:
            break

        if awin == 3:
            end = f"A won {awin}:{bwin} set"
        elif bwin == 3:
            end = f"B won {bwin}:{awin} set"

    if end:
        print(end)
    else:
        print(f"Set {g_set}: A ({score_a}) | B ({score_b})")
        print("The game has not finished yet.")

main(input())
