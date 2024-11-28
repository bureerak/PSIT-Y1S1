""" Diamond I """
def find_max_diamond(row, colum):
    """ return best column """
    mine = [input().split() for _ in range(row)]
    null = [0]*colum
    for i in range(row):
        for j in range(colum):
            null[j] += int(mine[i][j])
    print(max(null))
find_max_diamond(int(input()), int(input()))
