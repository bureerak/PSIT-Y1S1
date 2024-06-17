"""docstring"""
def main():
    """main function"""
    name = input()
    old = int(input())
    exp = int(input())
    if 15 <= old <= 60:
        if old < 21:
            permit = input()
            if permit == "No":
                return print(f"{name}, you aren't accepted.")
        if old >= 50 and exp < 5:
            return print(f"{name}, you aren't accepted.")
        if exp >= 6:
            return print(f"{name}, you're Master universal Cruz of Cruz Industries Enterprise.")
        if exp >= 3 :
            return print(f"{name}, you're Advance Cruz of Cruz Industries Enterprise.")
        return print(f"{name}, you're Newbie Cruz of Cruz Industries Enterprise.")
    return print(f"{name}, you aren't accepted.")
main()
