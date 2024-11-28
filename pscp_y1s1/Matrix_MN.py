"""Matrix_MN problem via iJudge during pair programming"""
def build_matrix():
    """
    This functions builds a matrix from the given size, member.

    Arguments:
    - m (int): Amount of rows
    - n (int): Amount of collumns
    - another m * n lines (str): Members in the built matrix

    Returns:
    - Matrix: Built matrix

    Raises:
       None.
    """
    m_row = int(input())
    n_col = int(input())

    fprint = [[ input() for _ in range(n_col)] for _ in range(m_row)]
    for i in fprint:
        print(*i)

    # for _ in range(m):
    #     num = input()
    #     for _ in range(n):
    #         print(num,end= ' ')
    #     print()
build_matrix()
