"""Summer CAT"""
def main():
    """function main"""
    fuel = float(input())
    distance = float(input())
    if fuel > 5:
        print("Impossible!!!")
    elif fuel*5 >= distance:
        print("You have enough fuel to get to Teimo's shop.")
    else:
        print("You do not have enough fuel to get to Teimo's shop.")
main()
