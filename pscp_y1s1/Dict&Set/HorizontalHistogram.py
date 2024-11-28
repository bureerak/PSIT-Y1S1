""" Histrogram can be better """
def gmm_grammy( text:str ):
    """ histrogrammer """
    a2z, res = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", {}
    for i in a2z:
        if i in text:
            res[i] = text.count( i )
    for i, j  in res.items():
        verti, count = '', divmod(j,5)
        verti += "-----|" * ( count[0] ) if count[1] else "-----|" * ( count[0] - 1) + "-----"
        verti += "-" * count[1]
        print( i,':',verti)
gmm_grammy( input() )
