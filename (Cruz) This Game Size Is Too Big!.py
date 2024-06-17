"""GB Calculate"""
def main():
    """Game Cal function"""
    game = float(input())
    storage = float(input())
    percentage = game/storage
    print(f"This game size is {percentage:.2%} of your directory size")
main()
