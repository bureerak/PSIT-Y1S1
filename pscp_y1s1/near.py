""" Find the Nearest Person """
def is_nearest(alice,bob,car):
    """ find nearest person between car """
    alice_dis = abs(car - alice)
    bob_dis = abs(car - bob)
    if alice_dis == bob_dis:
        print("Sundaes",end=" ")
    elif alice_dis < bob_dis:
        print("Alice",end=" ")
    else:
        print("Bob",end=" ")
    print(min(alice_dis,bob_dis))
is_nearest(int(input()),int(input()),int(input()))
