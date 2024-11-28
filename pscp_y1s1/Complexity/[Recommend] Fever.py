""" [Recommend] Fever """
def main():
    """ main function """
    cels = float( input() )
    degree = [(40,"Very High Fever"),(39,"High Fever"),(38,"Mild Fever"),(36,"No Fever")]
    for i,j in degree:
        if cels >= i:
            print(j)
            return
main()
