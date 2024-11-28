""" Diamond Head """
def max_diamond(m_row, n_colum):
    """ return most diamond path """
    dp = [[0]*n_colum for _ in range(m_row)]
    mine = [input().split() for _ in range(m_row)]
    for sublist in range(m_row):
        for i in range(n_colum):
            mine[sublist][i] = int(mine[sublist][i])

    for i in range(n_colum):
        dp[0][i] = mine[0][i]

    for i in range(1,m_row):
        for j in range(n_colum):
            max_value = int(dp[i-1][j])
            if j-1 >= 0:
                max_value = max(max_value,int(dp[i-1][j-1]))
            if j+1 <= n_colum-1:
                max_value = max(max_value,int(dp[i-1][j+1]))
            dp[i][j] = max_value+int(mine[i][j])
    print(max(dp[m_row-1]))

max_diamond(int(input()), int(input()))
