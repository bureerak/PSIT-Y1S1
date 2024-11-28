""" Amefuri Plus """
def amefuri(start,weather):
    """return cloth status"""
    moisture = 8
    for i in weather:
        if not moisture:
            break
        if i == "h":
            return print("Lost")
        for j,k in (("r",2),("s",3)):
            if i == j:
                moisture=min(16,moisture+k)
        table = (("c",0.25),("n",0.50),("w",0.75))
        if 6 <= start < 18:
            table = (("c",0.50),("n",1.00),("w",1.50))
        for j,k in table:
            if i == j:
                moisture=max(0,moisture-k)
        start=(start+1)%24
    return print(f"Still Wet (Wet Level: {moisture:.2f})" if moisture else "Dry")
amefuri(int(input()),input().lower())
