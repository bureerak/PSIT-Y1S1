""" Hello Kitty """
def payphone(number,form):
    """ formal form """
    lenght = len(number)
    wait = ""
    if form == "International":
        if lenght == 9:
            wait+="+66 "
        else:
            wait+=f"+66{number[1:lenght-8]} "
    else:
        wait+=f"{number[:lenght-8]} "
    wait+=f"{number[lenght-8:lenght-4]} {number[lenght-4:]}"
    print(wait)
payphone(input(),input())
