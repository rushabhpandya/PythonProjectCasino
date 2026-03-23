import random
import time

def play_wheel(balance):
    print("\n" + "="*40)
    print("        🎡  WHEEL GAME  🎡")
    print("="*40)

    if balance <= 0:
        print("❌ You have no balance left!")
        return balance

    print(f"\n💰 Your balance: ${balance}")
    print("\nWheel segments:")
    print("  🔴 0x  - Lose (3 segments)")
    print("  🟡 1.5x - Small win (2 segments)")
    print("  🟢 2x  - Win (2 segments)")
    print("  🔵 3x  - Big win (1 segment)")
    print("  💎 5x  - Jackpot (1 segment)")

    while True:
        try:
            bet = int(input("\nEnter your bet: $"))
            if bet <= 0:
                print("❌ Bet must be more than 0!")
            elif bet > balance:
                print(f"❌ You only have ${balance}!")
            else:
                break
        except ValueError:
            print("❌ Enter a valid number!")

    wheel = [0, 0, 0, 1.5, 1.5, 2, 2, 3, 5]
    
    print("\nSpinning the wheel", end="")
    for _ in range(5):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()

    # Spinning animation
    for _ in range(6):
        fake = random.choice(wheel)
        print(f"\r🎡 ...{fake}x...", end="", flush=True)
        time.sleep(0.3)

    result = random.choice(wheel)
    print(f"\r🎡 Landed on: {result}x!     ")

    if result == 0:
        balance -= bet
        print(f"\n❌ You LOST! -{bet}")
    elif result == 5:
        winnings = int(bet * result)
        balance = balance - bet + winnings
        print(f"\n💎 JACKPOT! You won ${winnings}!")
    else:
        winnings = int(bet * result)
        balance = balance - bet + winnings
        print(f"\n✅ You WON ${winnings}!")

    print(f"💰 New balance: ${balance}")
    print("="*40)
    return balance