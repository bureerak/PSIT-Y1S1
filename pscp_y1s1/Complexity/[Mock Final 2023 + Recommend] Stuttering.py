""" shutdown """
def main():
    """ main """
    sole = input().split()
    prev = None
    for i in sole:
        if prev == i:
            continue
        print(i,end=" ")
        prev = i
main()
