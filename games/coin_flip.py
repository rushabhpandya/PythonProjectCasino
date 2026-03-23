import random
import time

def play_coin_flip(balance):
    print("\n" + "="*40)
    print("        🪙  COIN FLIP  🪙")
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

    print("\nPick your side:")
    print("  1. Heads")
    print("  2. Tails")
    
    while True:
        choice = input("Your choice (1/2): ")
        if choice in ["1", "2"]:
            break
        print("❌ Enter 1 or 2!")

    player_choice = "Heads" if choice == "1" else "Tails"
    print(f"\n🪙 You picked: {player_choice}")
    print("Flipping", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

    result = random.choice(["Heads", "Tails"])
    print(f"\n🪙 It's... {result.upper()}!")

    if player_choice == result:
        balance += bet
        print(f"✅ You WON! +${bet}")
    else:
        balance -= bet
        print(f"❌ You LOST! -${bet}")

    print(f"💰 New balance: ${balance}")
    print("="*40)
    return balance