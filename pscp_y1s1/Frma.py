""" BigFrame """
def buildframe():
    """ build frame """
    text1,text2 = input().strip(),input().strip()
    text3,text4 = input().strip(),input().strip()
    text5 = input().strip()
    most = (max(len(text1),len(text2),len(text3),len(text4),len(text5)))
    print("****"+"*"*most)
    print(f"* {text1:<{most}} *")
    print(f"* {text2:<{most}} *")
    print(f"* {text3:<{most}} *")
    print(f"* {text4:<{most}} *")
    print(f"* {text5:<{most}} *")
    print("****"+"*"*most)
buildframe()
