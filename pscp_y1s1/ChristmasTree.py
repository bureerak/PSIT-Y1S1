""" if christmas tree are chris and how we call it if it change they religion? """
def main():
    """ main function """
    n_leaf = int(input())
    k_log = int(input())
    for i in range(1,n_leaf+1):
        print(" " * ( n_leaf - i ),"*" * ((i*2)-1),sep="")
    for _ in range(1,k_log+1):
        print(" "*(n_leaf-2),"---",sep="")
main()
