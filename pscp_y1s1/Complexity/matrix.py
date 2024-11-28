""" matrix pattern """
def main():
    """ main function """
    p_num = int( input() )
    q_num = int( input() )
    r_num = int( input() )
    mat_a = [[int(input()) for _ in range(q_num)] for _ in range(p_num)]
    mat_b = [[int(input()) for _ in range(r_num)] for _ in range(q_num)]
    mat_b = list(zip(*mat_b))
    for i in mat_a:
        for j in mat_b:
            print(sum(list(map(lambda a,b : a*b,i,j))),end=" ")
        print()
main()
