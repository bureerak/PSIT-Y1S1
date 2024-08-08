"""A"""
light = int(input())
height = int(input())
space = height//2
ROW=1
while ROW <= height:
    print(" " * abs(space),end="")
    print("*" * light)
    space=space-1
    ROW+=1
