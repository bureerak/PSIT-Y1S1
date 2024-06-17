"""Mixue but เกสตาโปแมน"""
def main():
    """mixue"""
    height = int(input())
    flavor = input()
    simp = height-1
    for i in range(height):
        for j in range((height*2)-1):
            if j >= height+i:
                continue
            if j == height - 1 or simp - i <= j <= simp + i:
                print(flavor,end="")
            else:
                print(" ",end="")
        print("")

    for i in range(height):
        if height == 1:
            print("_")
            break
        if i == height-1:
            break
        for j in range((height*2)-1):
            if j >= height*2-2-i:
                continue
            if height-(height-(i+1)) <= j < height*2-2-i:
                print("_",end="")
            else:
                print(" ",end="")
        print("")
main()
