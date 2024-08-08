""" Docstring """
def main():
    """ a """
    time = input()
    if time.isdigit() and int(time)//86400 < 10000:
        time = int(time)
        day = time // 86400
        time -= day * 86400
        hour = time // 3600
        time -= hour * 3600
        minute = time // 60
        time -= minute * 60
        print(f"{day:>04}:{hour:>02}:{minute:>02}:{time:>02}")
    else:
        print("ERR_:__:__:__")
main()
