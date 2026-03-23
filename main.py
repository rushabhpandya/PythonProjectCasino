from games.wheel_game import play_wheel
from games.coin_flip import play_coin_flip
from games.dice_game import play_dice
from games.blackjack import play_blackjack
from games.mines import play_mines

def main():
    balance = 1000
    while True:
        print("\n" + "="*40)
        print("      🎰  MINI STAKE CASINO  🎰")
        print("="*40)
        print(f"💰 Balance: ${balance}")
        print("\n1. Wheel Game")
        print("2. Dice Game")
        print("3. Coin Flip")
        print("4. Blackjack")
        print("5. Mines")
        print("6. Exit")
        print("="*40)
        choice = input("Choose a game: ")
        if choice == "1":
            balance = play_wheel(balance)
        elif choice == "2":
            balance = play_dice(balance)
        elif choice == "3":
            balance = play_coin_flip(balance)
        elif choice == "4":
            balance = play_blackjack(balance)
        elif choice == "5":
            balance = play_mines(balance)
        elif choice == "6":
            print("\n👋 Thanks for playing! Goodbye!")
            break

main()