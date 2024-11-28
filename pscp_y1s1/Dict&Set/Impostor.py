""" Impostor """
def amongus():
    """ SuS """
    on_ship,space = {}, {}
    while True:
        temp_in = input()
        if temp_in == "Start":
            break
        temp_in = temp_in.split('"')
        on_ship.update({temp_in[1]:temp_in[3]})

    imposter = list(on_ship.values()).count("Impostor")

    while True:
        temp_in = input()
        if temp_in == "End":
            break
        imposter = imposter - 1 if on_ship[temp_in] == "Impostor" else imposter
        space[temp_in] = on_ship.pop(temp_in)

    print(f"{imposter} Impostor Remains\n***Alive***")
    for i in sorted(on_ship.items()):
        print(f"{i[0]} : {i[1]}")
    print("***Dead***")
    for i in sorted(space.items()):
        print(f"{i[0]} : {i[1]}")

amongus()
