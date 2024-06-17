"""F TAXi"""
def taxi(distance):
    """Taxi Money"""
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
    return money
def main():
    """main function"""
    per1 = int(input())
    per2 = int(input())
    per3 = int(input())
    print(f"At Cha-ngon's home: {taxi(per1):.2f} baht")
    print(f"Cha-ngon pay {round(taxi(per1)/3):.2f} baht.")
    print(f"At Laong-Dao's home: {taxi(per2):.2f} baht")
    print(f"Laong-Dao pay {round(taxi(per2)/2):.2f} baht.")
    print(f"At Sakao-Duean's home: {taxi(per3):.2f} baht")
    print(f"Sakao-Duean pay {taxi(per3)-round(taxi(per2)/2)-round(taxi(per1)/3):.2f} baht.")
main()
