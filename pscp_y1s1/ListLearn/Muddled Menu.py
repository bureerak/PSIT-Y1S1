""" Muddle Menu """
def chef_order():
    """ return menu """
    order = []
    while True:
        x = input()
        if x == "SOMETHING'S WRONG":
            order.clear()
            continue
        if "Can't do:" in x:
            order.remove(x[10:])
            continue
        if x in ("CLOSED","DONE"):
            break
        pos = x[x.find("#")+1:]
        if pos == "N":
            order.append(x[:x.find("#") - 1])
        else:
            order.insert(int(x[x.find("#")+1:]) - 1, x[:x.find("#") -1])
    if x == "CLOSED":
        order.clear()
    res = reversed(order)
    print(f"Full Course: {order} Reversed: {list(res)}")
chef_order()
