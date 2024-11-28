""" Remove Tag """
def main(text):
    """ main function """
    state, ans = True, ""
    for i in text:
        if i == ">":
            state = True
            continue
        if i == "<":
            state = False
            ans+=" "
        if state:
            ans+=i
    print(ans.strip().split())
main( input() )
