from games.wheel_game import play_wheel
from games.coin_flip import play_coin_flip
from games.dice_game import play_dice
from games.blackjack import play_blackjack
from games.mines import play_mines
from database.player import login, register, save_player, get_leaderboard

def show_leaderboard():
    print("\n" + "="*40)
    print("        🏆  LEADERBOARD  🏆")
    print("="*40)
    players = get_leaderboard()
    if not players:
        print("No players yet!")
    for i, (name, balance, wins) in enumerate(players, 1):
        print(f"{i}. {name} - 💰${balance} - ✅{wins} wins")
    print("="*40)
    input("\nPress Enter to continue...")

def auth_menu():
    while True:
        print("\n" + "="*40)
        print("      🎰  MINI STAKE CASINO  🎰")
        print("="*40)
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        print("="*40)
        choice = input("Choose: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            data, msg = login(username, password)
            print(msg)
            if data:
                return username, data

        elif choice == "2":
            username = input("Choose username: ")
            password = input("Choose password: ")
            data, msg = register(username, password)
            print(msg)
            if data:
                return username, data

        elif choice == "3":
            exit()

def main():
    username, player = auth_menu()

    while True:
        print("\n" + "="*40)
        print("      🎰  MINI STAKE CASINO  🎰")
        print("="*40)
        print(f"👤 Player: {username}")
        print(f"💰 Balance: ${player['balance']}")
        print(f"✅ Wins: {player['wins']}  ❌ Losses: {player['losses']}")
        print("\n1. Wheel Game")
        print("2. Dice Game")
        print("3. Coin Flip")
        print("4. Blackjack")
        print("5. Mines")
        print("6. 🏆 Leaderboard")
        print("7. Exit")
        print("="*40)
        choice = input("Choose a game: ")

        old_balance = player['balance']

        if choice == "1":
            player['balance'] = play_wheel(player['balance'])
        elif choice == "2":
            player['balance'] = play_dice(player['balance'])
        elif choice == "3":
            player['balance'] = play_coin_flip(player['balance'])
        elif choice == "4":
            player['balance'] = play_blackjack(player['balance'])
        elif choice == "5":
            player['balance'] = play_mines(player['balance'])
        elif choice == "6":
            show_leaderboard()
            continue
        elif choice == "7":
            save_player(username, player)
            print(f"\n👋 Goodbye {username}! Progress saved!")
            break

        if player['balance'] > old_balance:
            player['wins'] += 1
        elif player['balance'] < old_balance:
            player['losses'] += 1

        save_player(username, player)

main()