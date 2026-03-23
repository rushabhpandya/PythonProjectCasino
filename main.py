from games.wheel_game import play_wheel
from games.coin_flip import play_coin_flip
from games.dice_game import play_dice
from games.blackjack import play_blackjack
from games.mines import play_mines
from database.player import login, register, save_player, get_leaderboard
from database.colors import *
import time

def show_leaderboard():
    print("\n" + bold_yellow("="*40))
    print(bold_yellow("        🏆  LEADERBOARD  🏆"))
    print(bold_yellow("="*40))
    players = get_leaderboard()
    if not players:
        print(red("No players yet!"))
    for i, (name, balance, wins) in enumerate(players, 1):
        if i == 1:
            print(bold_yellow(f"🥇 {i}. {name} - 💰${balance} - ✅{wins} wins"))
        elif i == 2:
            print(white(f"🥈 {i}. {name} - 💰${balance} - ✅{wins} wins"))
        elif i == 3:
            print(yellow(f"🥉 {i}. {name} - 💰${balance} - ✅{wins} wins"))
        else:
            print(cyan(f"   {i}. {name} - 💰${balance} - ✅{wins} wins"))
    print(bold_yellow("="*40))
    input("\nPress Enter to continue...")

def auth_menu():
    while True:
        print("\n" + bold_cyan("="*40))
        print(bold_cyan("      🎰  MINI STAKE CASINO  🎰"))
        print(bold_cyan("="*40))
        print(green("1. Login"))
        print(yellow("2. Register"))
        print(red("3. Exit"))
        print(bold_cyan("="*40))
        choice = input("Choose: ")

        if choice == "1":
            username = input(cyan("Username: "))
            password = input(cyan("Password: "))
            data, msg = login(username, password)
            if data:
                print(bold_green(msg))
                return username, data
            else:
                print(bold_red(msg))

        elif choice == "2":
            username = input(cyan("Choose username: "))
            password = input(cyan("Choose password: "))
            data, msg = register(username, password)
            if data:
                print(bold_green(msg))
                return username, data
            else:
                print(bold_red(msg))

        elif choice == "3":
            print(bold_red("\n👋 Goodbye!"))
            exit()

def show_banner(username, balance, wins, losses):
    print("\n" + bold_cyan("="*40))
    print(bold_cyan("      🎰  MINI STAKE CASINO  🎰"))
    print(bold_cyan("="*40))
    print(cyan(f"👤 Player: ") + bold_yellow(username))
    print(cyan(f"💰 Balance: ") + bold_green(f"${balance}"))
    print(green(f"✅ Wins: {wins}") + "  " + red(f"❌ Losses: {losses}"))
    print(bold_cyan("-"*40))
    print(bold_yellow("1.") + " 🎡 Wheel Game")
    print(bold_yellow("2.") + " 🎲 Dice Game")
    print(bold_yellow("3.") + " 🪙 Coin Flip")
    print(bold_yellow("4.") + " 🃏 Blackjack")
    print(bold_yellow("5.") + " 💣 Mines")
    print(bold_yellow("6.") + " 🏆 Leaderboard")
    print(bold_yellow("7.") + " 🚪 Exit")
    print(bold_cyan("="*40))

def main():
    username, player = auth_menu()

    print(bold_green(f"\n🎉 Welcome to Mini Stake Casino, {username}!"))
    time.sleep(1)

    while True:
        show_banner(username, player['balance'], player['wins'], player['losses'])
        choice = input(cyan("Choose a game: "))

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
            print(bold_red(f"\n👋 Goodbye {username}! Progress saved!"))
            break
        else:
            print(bold_red("❌ Invalid choice!"))
            continue

        if player['balance'] > old_balance:
            player['wins'] += 1
        elif player['balance'] < old_balance:
            player['losses'] += 1

        save_player(username, player)

main()