"""Docstring"""
def main():
    """main function"""
    distant = int(input())
    ammo = int(input())
    upcage = input()
    insidejob = input()
    insidejob = insidejob[-1::-1]
    lowcage = input()

    bug = insidejob.count("*")
    for i in range(1,distant+1):
        if not bug or not ammo:
            break
        if insidejob[i] == "*" and ammo:
            insidejob = insidejob.replace("*"," ",1)
            ammo-=1
            bug-=1

    if bug:
        print(f"There are still {bug} bugs and {ammo} ammos left.")
    else:
        print("All bugs are gone, Ahahahahaah.")

    print(upcage)
    print(insidejob[-1::-1])
    print(lowcage)
main()
