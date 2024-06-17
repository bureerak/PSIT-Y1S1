"""Docstring"""
def main():
    """main function"""
    day = int(input())
    ddaily = day
    ticket = day//7
    day -= ticket*7
    daily = ticket*4
    for i in range(day):
        if i+1 in (2,4):
            daily+=1
        if i+1 == 6:
            daily+=2
    print(f"Daily Login rewards: {daily:,} Saint Quartz")

    qur = 0
    if ddaily >= 100:
        qur = 60 + (((ddaily-100)//50) * 30)
    else:
        for j in range(1,ddaily+1):
            if not j % 10 and j<51:
                qur+=4
            if not j % 75:
                qur+=10
            if not j % 100:
                qur+=30
    print(f"Total Login rewards: {qur:,} Saint Quartz")
    print(f"Total Saint Quartz: {qur+daily:,} Saint Quartz")
    print(f"Summon Ticket: {ticket:,} Ticket")
main()
