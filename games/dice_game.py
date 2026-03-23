import random
import time

def play_dice(balance):
    print("\n" + "="*40)
    print("        🎲  DICE GAME  🎲")
    print("="*40)

    if balance <= 0:
        print("❌ You have no balance left!")
        return balance

    print(f"\n💰 Your balance: ${balance}")
    print("\nBetting options:")
    print("  1. Guess exact number (x6 payout)")
    print("  2. Guess odd/even (x2 payout)")
    print("  3. Guess high(4-6) or low(1-3) (x2 payout)")

    while True:
        mode = input("\nChoose mode (1/2/3): ")
        if mode in ["1", "2", "3"]:
            break
        print("❌ Enter 1, 2 or 3!")

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

    if mode == "1":
        while True:
            try:
                guess = int(input("Guess a number (1-6): "))
                if 1 <= guess <= 6:
                    break
                print("❌ Enter a number between 1 and 6!")
            except ValueError:
                print("❌ Enter a valid number!")
        multiplier = 6

    elif mode == "2":
        print("1. Odd  2. Even")
        while True:
            guess = input("Your choice (1/2): ")
            if guess in ["1", "2"]:
                break
            print("❌ Enter 1 or 2!")
        guess = "odd" if guess == "1" else "even"
        multiplier = 2

    else:
        print("1. Low (1-3)  2. High (4-6)")
        while True:
            guess = input("Your choice (1/2): ")
            if guess in ["1", "2"]:
                break
            print("❌ Enter 1 or 2!")
        guess = "low" if guess == "1" else "high"
        multiplier = 2

    print("\nRolling", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

    result = random.randint(1, 6)
    dice_faces = {1:"⚀", 2:"⚁", 3:"⚂", 4:"⚃", 5:"⚄", 6:"⚅"}
    print(f"\n🎲 Rolled: {dice_faces[result]} ({result})")

    won = False
    if mode == "1":
        won = guess == result
    elif mode == "2":
        won = (guess == "odd" and result % 2 != 0) or (guess == "even" and result % 2 == 0)
    else:
        won = (guess == "low" and result <= 3) or (guess == "high" and result >= 4)

    if won:
        balance += bet * (multiplier - 1)
        print(f"✅ You WON! +${bet * (multiplier - 1)}")
    else:
        balance -= bet
        print(f"❌ You LOST! -${bet}")

    print(f"💰 New balance: ${balance}")
    print("="*40)
    return balance