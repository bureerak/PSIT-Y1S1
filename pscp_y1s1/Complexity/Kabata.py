""" Kabata """
def main(num:int):
    """ Kabata """
    for _ in range(num):
        text = input().replace('bakka',' ').replace('ta',' ')
        if text.find('baka') != -1:
            print('no')
            continue
        text = text.replace('ba',' ').replace('ka',' ').strip()
        print('yes' if not text else 'no')
main(int(input()))
