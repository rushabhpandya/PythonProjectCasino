import random
import time

def roll_animation():
    faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    for _ in range(8):
        print(f"\r  🎲 {random.choice(faces)}  ", end="", flush=True)
        time.sleep(0.1)

def play_dice(balance):
    print("\n" + "="*40)
    print("        🎲  DICE GAME  🎲")
    print("="*40)

    if balance <= 0:
        print("❌ You have no balance left!")
        return balance

    print(f"\n💰 Your balance: ${balance}")
    print("\nGame modes:")
    print("  1. Classic   - Guess exact number (x6 payout)")
    print("  2. Odd/Even  - Guess odd or even (x2 payout)")
    print("  3. High/Low  - Guess high(4-6) or low(1-3) (x2 payout)")
    print("  4. Multi     - Roll 3 dice, guess total range (x3 payout)")

    while True:
        mode = input("\nChoose mode (1/2/3/4): ")
        if mode in ["1", "2", "3", "4"]:
            break
        print("❌ Enter 1, 2, 3 or 4!")

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

    dice_faces = {1:"⚀", 2:"⚁", 3:"⚂", 4:"⚃", 5:"⚄", 6:"⚅"}
    won = False
    multiplier = 1

    if mode == "1":
        while True:
            try:
                guess = int(input("Guess a number (1-6): "))
                if 1 <= guess <= 6:
                    break
                print("❌ Enter between 1 and 6!")
            except ValueError:
                print("❌ Enter a valid number!")
        multiplier = 6
        roll_animation()
        result = random.randint(1, 6)
        print(f"\r  🎲 {dice_faces[result]}  ({result})")
        won = guess == result

    elif mode == "2":
        print("1. Odd   2. Even")
        while True:
            guess = input("Your choice (1/2): ")
            if guess in ["1", "2"]:
                break
            print("❌ Enter 1 or 2!")
        guess = "odd" if guess == "1" else "even"
        multiplier = 2
        roll_animation()
        result = random.randint(1, 6)
        print(f"\r  🎲 {dice_faces[result]}  ({result})")
        won = (guess == "odd" and result % 2 != 0) or (guess == "even" and result % 2 == 0)

    elif mode == "3":
        print("1. Low (1-3)   2. High (4-6)")
        while True:
            guess = input("Your choice (1/2): ")
            if guess in ["1", "2"]:
                break
            print("❌ Enter 1 or 2!")
        guess = "low" if guess == "1" else "high"
        multiplier = 2
        roll_animation()
        result = random.randint(1, 6)
        print(f"\r  🎲 {dice_faces[result]}  ({result})")
        won = (guess == "low" and result <= 3) or (guess == "high" and result >= 4)

    elif mode == "4":
        print("\n🎲 You will roll 3 dice!")
        print("Guess the total range:")
        print("  1. Low   (3-8)")
        print("  2. Mid   (9-12)")
        print("  3. High  (13-18)")
        while True:
            guess = input("Your choice (1/2/3): ")
            if guess in ["1", "2", "3"]:
                break
            print("❌ Enter 1, 2 or 3!")
        guess = {"1": "low", "2": "mid", "3": "high"}[guess]
        multiplier = 3

        print("\nRolling 3 dice", end="")
        results = []
        for i in range(3):
            time.sleep(0.4)
            r = random.randint(1, 6)
            results.append(r)
            print(f"  {dice_faces[r]}", end="", flush=True)
        
        total = sum(results)
        print(f"\n\n🎲 Dice: {' '.join(dice_faces[r] for r in results)}")
        print(f"📊 Total: {total}")

        if guess == "low":
            won = total <= 8
        elif guess == "mid":
            won = 9 <= total <= 12
        else:
            won = total >= 13

    if won:
        balance += bet * (multiplier - 1)
        print(f"\n✅ You WON! +${bet * (multiplier - 1)}")
    else:
        balance -= bet
        print(f"\n❌ You LOST! -${bet}")

    print(f"💰 New balance: ${balance}")
    print("="*40)
    return balance