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
        print(f"  {name}: [{hand[0]}, ???]")
    else:
        print(f"  {name}: {hand} = {hand_value(hand)}")

def play_hand(hand, name, balance, bet):
    while True:
        display_hand(name, hand)
        if hand_value(hand) == 21:
            print(f"  🎉 Blackjack on {name}!")
            break
        if hand_value(hand) > 21:
            print(f"  💥 {name} busted!")
            break

        print(f"\n  {name} options:")
        print("    1. Hit")
        print("    2. Stand")
        if len(hand) == 2 and balance >= bet * 2:
            print("    3. Double Down")

        action = input("  Your choice: ")

        if action == "1":
            hand.append(get_card())
            display_hand(name, hand)
            if hand_value(hand) > 21:
                print(f"  💥 {name} busted!")
                break

        elif action == "2":
            break

        elif action == "3" and len(hand) == 2:
            bet *= 2
            hand.append(get_card())
            print(f"  💰 Bet doubled to ${bet}")
            display_hand(name, hand)
            break

    return hand, bet

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

    # Blackjack check
    if hand_value(player) == 21:
        print("\n🎉 BLACKJACK! You win instantly!")
        payout = int(bet * 1.5)
        balance += payout
        print(f"✅ You WON! +${payout}")
        print(f"💰 New balance: ${balance}")
        return balance

    # Split option
    hands = [player]
    bets = [bet]

    if player[0] == player[1] and balance >= bet * 2:
        print(f"\n✂️  You have a pair of {player[0]}s!")
        split = input("Do you want to SPLIT? (y/n): ")
        if split.lower() == "y":
            hands = [[player[0], get_card()], [player[1], get_card()]]
            bets = [bet, bet]
            balance -= bet
            print(f"💰 Split! Playing 2 hands. Balance: ${balance}")

    # Play each hand
    final_hands = []
    final_bets = []
    for i, (hand, b) in enumerate(zip(hands, bets)):
        if len(hands) > 1:
            print(f"\n--- Hand {i+1} ---")
        hand, b = play_hand(hand, f"Hand {i+1}" if len(hands) > 1 else "You", balance, b)
        final_hands.append(hand)
        final_bets.append(b)

    # Dealer turn
    print("\n--- Dealer's Turn ---")
    display_hand("Dealer", dealer)
    time.sleep(0.5)
    while hand_value(dealer) < 17:
        print("  Dealer hits...")
        time.sleep(0.5)
        dealer.append(get_card())
        display_hand("Dealer", dealer)

    dealer_val = hand_value(dealer)

    # Results
    print("\n--- Results ---")
    for i, (hand, b) in enumerate(zip(final_hands, final_bets)):
        label = f"Hand {i+1}" if len(final_hands) > 1 else "You"
        player_val = hand_value(hand)
        print(f"\n  {label}: {player_val} vs Dealer: {dealer_val}")

        if player_val > 21:
            balance -= b
            print(f"  💥 Bust! -${b}")
        elif dealer_val > 21:
            balance += b
            print(f"  ✅ Dealer busts! +${b}")
        elif player_val > dealer_val:
            balance += b
            print(f"  ✅ You win! +${b}")
        elif player_val < dealer_val:
            balance -= b
            print(f"  ❌ You lose! -${b}")
        else:
            print(f"  🤝 Tie! Bet returned.")

    print(f"\n💰 New balance: ${balance}")
    print("="*40)
    return balance