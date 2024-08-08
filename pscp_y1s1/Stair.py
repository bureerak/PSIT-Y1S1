""" stair stood stood """
def main():
    """ main function """
    max_range = int( input() )
    stair = int( input() )
    step, gap= 0, 0
    for _ in range(stair):
        all_step = int(input())
        if all_step > max_range:
            break
        gap+=all_step
        if gap == max_range:
            step+=1
            gap=0
        elif gap > max_range:
            step+=1
            gap=all_step
    if gap <= max_range and gap:
        step+=1
    print("NO" if all_step>max_range else step)
main()
