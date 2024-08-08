""" RPS Week 5 """
def main(duel = input()):
    """ main function """
    lenght = len(duel)
    player1 , player2 = 0, 0
    for i in range(0,lenght-1,2):
        if duel[i] == duel[i+1]:
            continue
        if duel[i:i+2] in ("RS","SP","PR"):
            player1 += 1
        else:
            player2 +=1
    if player1 == player2:
        print("DRAW",player1)
    else:
        print("A" if player1>player2 else "B",end=" ")
        print(f"win {max(player1,player2)}-{min(player1,player2)}")
main()
