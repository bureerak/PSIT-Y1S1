"""Mein Kraft"""
import math as ma
def skill(name,hp,dmg):
    """skill"""
    total = 0
    if name == "Mining":
        total = (dmg * (dmg/hp))*2
        total = ma.ceil(total)
        return total
    if name == "Special":
        total = (ma.ceil((dmg * (dmg/hp))*2) + 10)*3
        total = total//1
        return total
    if name == "TNT":
        total = (hp/3) * ma.ceil((dmg * (dmg/hp))*2)
        total = total//1
        return total
    return total
def main():
    """main function"""
    count = 0
    hp = float(input())
    dmg = float(input())
    while count < 3 and hp > 0:
        selec = input()
        count+=1
        if selec in ("Mining","Special","TNT"):
            if selec == "Special":
                print(f"Use {selec} Attack deal {skill(selec,hp,dmg)} damage.")
            else:
                print(f"Use {selec} deal {skill(selec,hp,dmg)} damage.")
            hp-=skill(selec,hp,dmg)
            if hp > 0:
                print(f"Ore's health is {hp:.2f}. We need to dig in more.")
            else:
                print(f"Ore's health is down to {hp:.2f}. We Succesfully mined the ore.")
                break
        else:
            print("We don't know that skill.")
            print(f"Ore's health is {hp:.2f}. We need to dig in more.")
main()
