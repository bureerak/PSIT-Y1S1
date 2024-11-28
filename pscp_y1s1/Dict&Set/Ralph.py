""" Ralph Breaks the Internet : Wreck-It Ralph 2 """
def main():
    """ main function """
    text = input()
    null = {}
    for i in text:
        if i.isalpha():
            null[i] = null.get(i,0)+1
    most = max(null.values())
    graph = sorted(null)
    for i in range(most,0,-1):
        print(f"{i:>2}","",end="")
        for j in graph:
            print(" *" if null[j] >= i else "  ",end="")
        print()
    print("  ",'',*graph,end="")
main()
