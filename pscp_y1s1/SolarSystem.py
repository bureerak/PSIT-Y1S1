""" SolarSys """
def planet(solar = input()):
    """ find planet close and far from sun """
    solar = " "+solar+" "
    sun = solar.find(" Sun ")
    solar = solar.strip()
    ldist = solar.count(" ",0,sun)
    rdist = solar.count(" ",sun)

    hotest = ""
    if ldist:
        lhot = solar[:sun-1][-((solar[:sun-1])[::-1]+" ").find(" "):]
        lhot = lhot.strip()
        hotest += lhot+" " if lhot else solar[:solar.find(" ")]+" "
    if rdist:
        rhot = solar[solar.find(" ",sun)+1:(solar+" ").find(" ",sun+4)]
        rhot = rhot.strip()
        hotest += rhot if rhot else solar[sun+4:]
    solar = solar.strip()

    if ldist > rdist:
        coldest = solar[:solar.find(" ")]
    elif ldist < rdist:
        coldest = solar[-(solar[::-1].find(" ")):]
    else:
        coldest = solar[:solar.find(" ")]+" "+solar[-(solar[::-1].find(" ")):]

    print(f"Hot: {hotest}".strip())
    print(f"Cool: {coldest}".strip())
planet()
