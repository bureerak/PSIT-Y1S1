"""LoL Rank Divisor Program"""
def main():
    """Main function"""
    rank = input()
    if rank == "Iron":
        print("Iron Bronze Silver")
    elif rank == "Bronze":
        print("Iron Bronze Silver")
    elif rank == "Silver":
        print("Iron Bronze Silver Gold")
    elif rank == "Gold":
        print("Silver Gold Platinum")
    elif rank == "Platinum":
        print("Gold Platinum Emerald")
    elif rank == "Emerald":
        print("Platinum Emerald Diamond")
    elif rank == "Diamond":
        print("Emerald Diamond")
    elif rank == "Master":
        print("Solo Only!!")
    elif rank == "Grandmaster":
        print("Solo Only!!")
    elif rank == "Challenger":
        print("Solo Only!!")
    else:
        print("Error please enter your rank again!")
main()
