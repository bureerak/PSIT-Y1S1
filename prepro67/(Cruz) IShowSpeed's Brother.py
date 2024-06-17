"""IshowSPD bro"""
def main():
    """Mainfunction"""
    x_1 = int(input())
    x_2 = int(input())
    time = int(input())
    velocity = (x_2-x_1)/time
    print(f"The Velocity is {velocity:.2f} m/s")
main()
