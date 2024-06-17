"""F TAXi"""
def main():
    """Taxi Function"""
    distance = int(input())
    money = 0
    if distance > 80:
        distance -= 80
        money = 35+58.5+70+160+170+180 + distance*10.5
    elif distance > 60:
        distance -= 60
        money = 35+58.5+70+160+170 + distance*9
    elif distance > 40:
        distance -= 40
        money = 35+58.5+70+160 + distance*8.5
    elif distance > 20:
        distance -= 20
        money = 35+58.5+70 + distance*8
    elif distance > 10:
        distance -= 10
        money = 35+58.5 + distance*7
    elif distance > 1:
        distance -= 1
        money = 35 + distance*6.5
    elif distance == 1:
        money = 35
    print(f"{money:.2f}")
main()
