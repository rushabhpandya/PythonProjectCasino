import random
import time

def get_card():
    cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    return random.choice(cards)

def card_value(card):
    if card in ['J','Q','K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

def hand_value(hand):
    value = sum(card_value(c) for c in hand)
    aces = hand.count('A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(name, hand, hide_second=False):
    if hide_second:
        print(f"{name}'s hand: [{hand[0]}, ???]")
    else:
        print(f"{name}'s hand: {hand} = {hand_value(hand)}")

def play_blackjack(balance):
    print("\n" + "="*40)
    print("       🃏  BLACKJACK  🃏")
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

    player = [get_card(), get_card()]
    dealer = [get_card(), get_card()]

    print("\n--- Cards Dealt ---")
    display_hand("You", player)
    display_hand("Dealer", dealer, hide_second=True)

    # Check for blackjack
    if hand_value(player) == 21:
        print("\n🎉 BLACKJACK! You win instantly!")
        balance += int(bet * 1.5)
        print(f"✅ You WON! +${int(bet * 1.5)}")
        print(f"💰 New balance: ${balance}")
        return balance

    # Player turn
    while True:
        print("\nWhat do you want to do?")
        print("  1. Hit")
        print("  2. Stand")
        if len(player) == 2 and balance >= bet * 2:
            print("  3. Double Down")

        action = input("Your choice: ")

        if action == "1":
            player.append(get_card())
            display_hand("You", player)
            if hand_value(player) > 21:
                print("💥 BUST! You went over 21!")
                balance -= bet
                print(f"❌ You LOST! -${bet}")
                print(f"💰 New balance: ${balance}")
                return balance

        elif action == "2":
            break

        elif action == "3" and len(player) == 2:
            bet *= 2
            player.append(get_card())
            display_hand("You", player)
            print(f"💰 Bet doubled to ${bet}")
            if hand_value(player) > 21:
                print("💥 BUST! You went over 21!")
                balance -= bet
                print(f"❌ You LOST! -${bet}")
                print(f"💰 New balance: ${balance}")
                return balance
            break

    # Dealer turn
    print("\n--- Dealer's Turn ---")
    display_hand("Dealer", dealer)
    time.sleep(1)

    while hand_value(dealer) < 17:
        print("Dealer hits...")
        time.sleep(0.5)
        dealer.append(get_card())
        display_hand("Dealer", dealer)

    # Result
    player_val = hand_value(player)
    dealer_val = hand_value(dealer)

    print("\n--- Result ---")
    print(f"Your hand: {player_val}")
    print(f"Dealer hand: {dealer_val}")

    if dealer_val > 21:
        print("💥 Dealer busts!")
        balance += bet
        print(f"✅ You WON! +${bet}")
    elif player_val > dealer_val:
        balance += bet
        print(f"✅ You WON! +${bet}")
    elif player_val < dealer_val:
        balance -= bet
        print(f"❌ You LOST! -${bet}")
    else:
        print("🤝 It's a TIE! Bet returned.")

    print(f"💰 New balance: ${balance}")
    print("="*40)
    return balance