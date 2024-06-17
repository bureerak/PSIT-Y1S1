"""compass"""
def turn_left(dt):
    """turn left"""
    if dt == "North":
        return "West"
    if dt == "West":
        return "South"
    if dt == "South":
        return "East"
    if dt == "East":
        return "North"
    return dt
def turn_right(dt):
    """turn right"""
    if dt == "North":
        return "East"
    if dt == "West":
        return "North"
    if dt == "South":
        return "West"
    if dt == "East":
        return "South"
    return dt
def main():
    """main function"""
    direct = "North"
    command = ""
    while command != "Stop!!":
        command = input()
        if command == "Turn Left!":
            direct = turn_left(direct)
        if command == "Turn Right!":
            direct = turn_right(direct)
        if command == "Turn Around!":
            direct = turn_right(direct)
            direct = turn_right(direct)
    print(direct)
main()
