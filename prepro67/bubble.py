"""a"""
def main():
    """b"""
    text=input()
    start=text.index("^")
    text=text[start+1:]
    goal=len(text)
    current=0
    step=0

    text+="______"
    while goal > current:
        if text[current] == "|":
            step+=1
            print("POSSIBLE")
            print(step)
            break

        if text[current] == "o":
            step+=1
            current+=1

        if text[current] == "O":
            #สองก้าวรวบ
            step+=1
            jumpable=text[current+1:current+4]
            if jumpable == "   ":
                print("IMPOSSIBLE")
                print(goal-current-1)
                break

            if "O" in jumpable and (text[current+4] in (" ","|") or text[current+5] == "|"):
                for j in range(3)[::-1]:
                    if jumpable[j]=="O":
                        current += j+1
                        break
            else:
                for i in range(3)[::-1]:
                    if jumpable[i]=="o" or jumpable[i]=="O" or jumpable[i]=="|":
                        current += i+1
                        break

        if text[current] == " ":
            print("IMPOSSIBLE")
            print(goal-current)
            break
main()
