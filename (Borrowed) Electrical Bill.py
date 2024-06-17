"""Docstring"""
def main():
    """function main"""
    watt_a = int(input())
    watt_b = int(input())
    watt_c = int(input())
    watt_d = int(input())
    watt_e = int(input())
    print(f"TV {watt_a} Watt 1 ea for 3 hours")
    print(f"{((watt_a * 3)/1000)*30:.2f} unit.")
    print(f"Microwave {watt_b} Watt 1 ea for 1 hours")
    print(f"{(watt_b/1000)*30:.2f} unit.")
    print(f"Hair dryer {watt_c} Watt 1 ea for 0.5 hours")
    print(f"{((watt_c*0.5)/1000)*30:.2f} unit.")
    print(f"Light bulb {watt_d} Watt 4 ea for 5 hours")
    print(f"{((watt_d*4*5)/1000)*30:.2f} unit.")
    print(f"Refrigerator {watt_e} Watt 1 ea for 24 hours")
    print(f"{((watt_e*24)/1000)*30:.2f} unit.")
main()
