"""F TAXi"""
def main():
    """Taxi Function"""
    distance = int(input())
    money = 0
    if distance == 1:
        money = 35
    elif distance < 11:
        money = 35+(distance-1)*6.5
    elif distance < 21:
        money = 35+(9*6.5)+(distance-10)*7
    elif distance < 41:
        money = 35+(9*6.5)+(10*7)+(distance-20)*8
    elif distance < 61:
        money = 35+(9*6.5)+(10*7)+(20*8)+(distance-40)*8.5
    elif distance < 81:
        money = 35+(9*6.5)+(10*7)+(20*8)+(20*8.5)+(distance-60)*9
    else:
        money = 35+(9*6.5)+(10*7)+(20*8)+(20*8.5)+(20*9)+(distance-80)*10.5
    print(f"{money:.2f}")
main()
