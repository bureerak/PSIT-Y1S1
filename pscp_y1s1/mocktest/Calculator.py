""" calculator """
def main():
    """ main """
    num = int(input())
    space = ""
    for i in range(1,num+1):
        if num == 1:
            space+="1"
            break
        space+=f"{i}"
        space+="+"
    print(len(space))
main()
