"""KeyboardDistant"""
import math
def main():
    """holy"""
    row0 = "QWERTYUIOP"
    row1 = "ASDFGHJKL;"
    row2 = "ZXCVBNM,./"
    text = input()
    lenght = len(text)-1

    first = ""
    second = ""
    ans = 0

    for i in range(lenght):
        if text[i] in row0:
            first += f"{row0.find(text[i])}" + "0"
        if text[i] in row1:
            first += f"{row1.find(text[i])}" + "1"
        if text[i] in row2:
            first += f"{row2.find(text[i])}" + "2"

        if text[i+1] in row0:
            second += f"{row0.find(text[i+1])}" + "0"
        if text[i+1] in row1:
            second += f"{row1.find(text[i+1])}" + "1"
        if text[i+1] in row2:
            second += f"{row2.find(text[i+1])}" + "2"

        if first[1] == second[1]:
            ans += abs(int(first[0])-int(second[0]))
        else:
            a_1 = abs(int(first[0])-int(second[0]))
            b_1 = abs(int(first[1])-int(second[1]))
            ans+=math.sqrt(a_1**2+b_1**2)
        first = ""
        second = ""
    print(f"{round(ans,4):.4f}")
main()
