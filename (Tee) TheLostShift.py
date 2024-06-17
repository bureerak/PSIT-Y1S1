"""asfdfadsg"""
def main():
    """main function"""
    text = input()
    status = 0
    count = 0
    for i in text:
        if not status:
            if i.isupper():
                count+=1
                status=1
        if status == 1:
            if i.islower():
                count+=1
                status=0
    print(count)
main()
