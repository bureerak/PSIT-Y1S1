"""doc"""
def main():
    """a"""
    num = int(input())
    ptcp = {}
    vote = ""
    top_sc = 0
    gwin = []
    for _ in range(num):
        name = input()
        ptcp[name] = 0
    key = ptcp.keys()
    while vote != "End":
        vote = input()
        if vote in key:
            ptcp[vote] += 1
    for _,i in ptcp.items():
        if i > top_sc:
            top_sc = i
    for k,j in ptcp.items():
        if j == top_sc:
            gwin.append(k)
    lenght = len(gwin)
    if not top_sc:
        print("Don't have the winner because top score is 0.")
    elif lenght > 1:
        print("Can't find the winner.")
        sep = ", "
        gwin.sort()
        gwin = sep.join(gwin)
        print(f"Top score : {gwin}.")
    elif lenght == 1:
        gwin = gwin[0]
        print(f"The winner is {gwin}.")
main()
