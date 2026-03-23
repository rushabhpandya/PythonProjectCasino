import random
import time

def play_mines(balance):
    print("\n" + "="*40)
    print("        💣  MINES  💣")
    print("="*40)

    if balance <= 0:
        print("❌ You have no balance left!")
        return balance

    print(f"\n💰 Your balance: ${balance}")

    while True:
        try:
            bet = int(input("Enter your bet: $"))
            if bet <= 0:
                print("❌ Bet must be more than 0!")
            elif bet > balance:
                print(f"❌ You only have ${balance}!")
            else:
                break
        except ValueError:
            print("❌ Enter a valid number!")

    while True:
        try:
            num_mines = int(input("How many mines? (1-5): "))
            if 1 <= num_mines <= 5:
                break
            print("❌ Enter between 1 and 5!")
        except ValueError:
            print("❌ Enter a valid number!")

    total_cells = 25
    mines = random.sample(range(total_cells), num_mines)
    revealed = []
    multiplier = 1.0

    def display_grid(reveal_all=False):
        print("\n    1  2  3  4  5")
        print("  " + "-"*16)
        for row in range(5):
            print(f"{row+1} |", end="")
            for col in range(5):
                idx = row * 5 + col
                if idx in revealed:
                    if idx in mines:
                        print("💣 ", end="")
                    else:
                        print("💎 ", end="")
                elif reveal_all:
                    if idx in mines:
                        print("💣 ", end="")
                    else:
                        print("⬜ ", end="")
                else:
                    print("⬜ ", end="")
            print("|")
        print("  " + "-"*16)

    print("\n🎮 Reveal cells to increase your multiplier!")
    print("💣 Hit a mine and lose everything!")
    print("💰 Cash out anytime to keep your winnings!")
    print(f"⚠️  {num_mines} mines hidden in the grid!\n")

    while True:
        display_grid()
        gain = round(bet * multiplier, 2)
        print(f"\n📈 Current multiplier: {multiplier}x")
        print(f"💰 Cash out value: ${int(gain)}")
        print(f"💎 Cells revealed: {len(revealed)}")
        print("\nWhat do you want to do?")
        print("  1. Reveal a cell")
        print("  2. Cash out")

        action = input("Your choice: ")

        if action == "2":
            balance = balance - bet + int(gain)
            print(f"\n✅ Smart move! Cashed out ${int(gain)}!")
            display_grid(reveal_all=True)
            print(f"💰 New balance: ${balance}")
            print("="*40)
            return balance

        elif action == "1":
            while True:
                try:
                    row = int(input("Enter row (1-5): ")) - 1
                    col = int(input("Enter col (1-5): ")) - 1
                    if 0 <= row <= 4 and 0 <= col <= 4:
                        idx = row * 5 + col
                        if idx in revealed:
                            print("❌ Already revealed! Pick another!")
                        else:
                            break
                    else:
                        print("❌ Enter between 1 and 5!")
                except ValueError:
                    print("❌ Enter a valid number!")

            if idx in mines:
                revealed.append(idx)
                print("\n💥 BOOM! You hit a mine!")
                time.sleep(0.5)
                print("\n🔍 Revealing all mines...\n")
                time.sleep(0.5)
                display_grid(reveal_all=True)
                balance -= bet
                print(f"\n❌ You LOST! -${bet}")
                print(f"💰 New balance: ${balance}")
                print("="*40)
                return balance
            else:
                revealed.append(idx)
                multiplier = round(multiplier + (0.5 * num_mines), 2)
                print(f"\n💎 Safe! Multiplier is now {multiplier}x!")

        if len(revealed) == total_cells - num_mines:
            print("\n🎉 YOU CLEARED THE ENTIRE BOARD!")
            balance = balance - bet + int(bet * multiplier)
            display_grid(reveal_all=True)
            print(f"💰 New balance: ${balance}")
            print("="*40)
            return balance