""" Key """
def main(number = input()):
    """ main function """
    fst = 0
    sec = int(number[len(number)-3:]) * 10
    for i in number:
        fst += int(i)
    fusion = fst+sec
    if fusion < 1000:
        fusion+=1000
    fusion = str(fusion)
    fusion = fusion[len(fusion)-4:]
    print(fusion)
main()
