"""Dart problem via iJudge during pair programming"""
import math as m
def target_score():
    """
    This function calculates scores shot in the target.

    Arguments:
    - Darts (int): Amount of darts shot.
    - Another amount of darts line (str): Coords of each dart

    Returns:
    - sum (int): Total score

    Raises:
       None.
    """
    num = int(input())
    scores = 0
    for _ in range(num):
        coords = input().split()
        z = m.sqrt(int(coords[0])**2 + int(coords[1])**2)
        if 0 <= z <= 2:
            scores += 5
        elif 2 < z <= 4:
            scores += 4
        elif 4 < z <= 6:
            scores += 3
        elif 6 < z <= 8:
            scores += 2
        elif 8 < z <= 10:
            scores += 1
    print(scores)
target_score()
