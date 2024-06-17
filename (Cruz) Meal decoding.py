"""decode"""
def main():
    """main fucntion"""
    ans=""
    caution=0
    code = input()
    lenght = len(code)
    che = lenght//2
    if lenght%2:
        ans+=code[che]
        code = code[:che]+code[che+1:]
        lenght-=1
        caution+=1
    mid = lenght//2
    for i in range(mid):
        if caution == 1:
            ans += code[i]+code[mid+i]
        else:
            ans += code[mid+i]+code[i]
    print(ans)
main()
