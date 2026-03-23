print("Welcome to Mini Stake Casino!")

def main():
    balance = 1000
    while True:
        print("\n=== Mini Stake Casino ===")
        print(f"Balance: ${balance}")
        print("1. Wheel Game")
        print("2. Dice Game")
        print("3. Coin Flip")
        print("4. Blackjack")
        print("5. Mines")
        print("6. Exit")
        choice = input("Choose a game: ")
        if choice == "6":
            print("Thanks for playing!")
            break

main()