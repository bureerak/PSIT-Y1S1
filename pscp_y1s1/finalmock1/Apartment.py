import json
def main(lst, n, s):
    """ main function """
    length = len(lst)
    max_sum = 0
    for i in range(length):
        cur_sum = 0
        index = i
        for _ in range(n):
            cur_sum += lst[index]
            index = (index + s) % length
        max_sum = max(max_sum, cur_sum)
    print(max_sum)
main(json.loads(input()), int(input()), int(input()))
