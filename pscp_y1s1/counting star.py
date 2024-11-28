""" counting star """
def star_count(sky):
    """ return set of star """
    lenght = len(sky)
    cont,comet,shoot = 0,0,0
    sky += "_"
    for i in range(lenght):
        if sky[i]+sky[i+1] in ("~*","*~"):
            comet+=1
        elif sky[i]+sky[i+1] ==  "*/":
            shoot+=1
        elif sky[i]+sky[i+1] == "**":
            cont+=1
        if sky[i]+sky[i+1] in ("~*","*~","*/","**"):
            sky = sky.replace(f"{sky[i]}{sky[i+1]}","__",1)
    if not cont and not comet and not shoot:
        print("Tonight is a quiet night.")
    else:
        print(f"constellation: {cont}\ncomet: {comet}\nshooting star: {shoot}".strip())
star_count(input())
