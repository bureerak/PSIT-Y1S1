""" brick bridge """
def main(a = int( input() ), b = int( input() )):
    """ main function """
    goal = int( input() )
    use_b = goal//5

    if b >= use_b:
        cur_distant = use_b * 5
    else:
        cur_distant = b * 5

    if cur_distant + a < goal:
        print(-1)
    else:
        print(goal-cur_distant)
main()
