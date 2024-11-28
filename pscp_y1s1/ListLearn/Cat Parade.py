""" Cat Parade """
def main():
    """ main function """
    null, answer = [], []
    while True:
        x = input()
        if x == "END":
            break
        if x == "IT'S A DOG":
            null.pop()
            continue
        x = x.split(", ")
        null += x
    for i in null:
        if i not in answer:
            answer.append(i)
    answer.sort()
    for i in answer:
        print(f"{i} {null.index(i)+1} {null.count(i)}")
main()
