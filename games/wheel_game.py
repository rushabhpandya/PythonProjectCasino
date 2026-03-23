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
    print("  🔴 0x   - Lose       (3 segments)")
    print("  🟡 1.5x - Small win  (2 segments)")
    print("  🟢 2x   - Win        (2 segments)")
    print("  🔵 3x   - Big win    (1 segment)")
    print("  💎 5x   - JACKPOT    (1 segment)")

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
    segments = ["🔴 0x", "🔴 0x", "🔴 0x", "🟡 1.5x", "🟡 1.5x", "🟢 2x", "🟢 2x", "🔵 3x", "💎 5x"]

    print("\n🎡 Spinning the wheel...\n")
    time.sleep(0.5)

    # Animation
    spins = 20
    delay = 0.05
    for i in range(spins):
        idx = random.randint(0, len(segments)-1)
        print(f"\r  ▶ {segments[idx]}  ◀   ", end="", flush=True)
        time.sleep(delay)
        delay += 0.02

    # Final result
    final_idx = random.randint(0, len(wheel)-1)
    result = wheel[final_idx]
    print(f"\r  ▶ {segments[final_idx]}  ◀   ")
    print("\n" + "🎡 " * 10)

    time.sleep(0.5)

    if result == 0:
        balance -= bet
        print(f"\n💥 UNLUCKY! You lost ${bet}!")
    elif result == 5:
        winnings = int(bet * result)
        balance = balance - bet + winnings
        print(f"\n💎 JACKPOT!! You won ${winnings}! 🎉🎉🎉")
    else:
        winnings = int(bet * result)
        balance = balance - bet + winnings
        print(f"\n✅ Nice! You won ${winnings}! ({result}x)")

    print(f"💰 New balance: ${balance}")
    print("="*40)
    return balance