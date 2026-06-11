from datetime import datetime
import random
import json
import os

# ================= FILE HANDLING =================

try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    BASE_DIR = os.getcwd()

file_name = os.path.join(BASE_DIR, "files", "tic_tac_toe_game.json")

os.makedirs(os.path.dirname(file_name), exist_ok=True)


def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"matches": []}


def save_data(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


# ================= HISTORY =================

def show_history():
    data = load_data()

    if not data["matches"]:
        print("\nNo previous matches found.\n")
        return

    print("\n===== MATCH HISTORY =====\n")

    for index, match in enumerate(data.get("matches", []), start=1):

        print(f"\nMatch #{index}")
        print(f"Players : {match['player1']} vs {match['player2']}")
        print(f"Winner  : {match['winner']}")
        print(f"Day     : {match['day']}")
        print(f"Date    : {match['date']}")
        print(f"Time    : {match['time']}")
        print("-" * 40)


# ================= GAME =================

def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(board, symbol):

    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_positions:

        if (
            board[combo[0]] == symbol and
            board[combo[1]] == symbol and
            board[combo[2]] == symbol
        ):
            return True

    return False


def play_game():

    player1 = input("\nEnter First Player Name: ").strip()
    player2 = input("Enter Second Player Name: ").strip()

    toss_winner = random.choice([player1, player2])

    if toss_winner == player1:
        symbols = {
            player1: "X",
            player2: "O"
        }
    else:
        symbols = {
            player1: "O",
            player2: "X"
        }

    print(f"\n🎲 {toss_winner} won the toss!")

    print(f"{player1} = {symbols[player1]}")
    print(f"{player2} = {symbols[player2]}")

    current_player = toss_winner

    board = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
    ]

    for turn in range(9):

        display_board(board)

        symbol = symbols[current_player]

        while True:

            try:
                position = int(
                    input(
                        f"{current_player} ({symbol}) "
                        f"Enter position (1-9): "
                    )
                ) - 1

                if position < 0 or position > 8:
                    print("Invalid position.")
                    continue

                if board[position] in ["X", "O"]:
                    print("Position already occupied.")
                    continue

                board[position] = symbol
                break

            except ValueError:
                print("Please enter a number from 1-9.")

        if check_winner(board, symbol):

            display_board(board)

            print(f"\n🏆 {current_player} won the game!")

            data = load_data()

            now = datetime.now()

            data["matches"].append({
                "player1": player1,
                "player2": player2,
                "winner": current_player,
                "day": now.strftime("%A"),
                "date": now.strftime("%d-%m-%Y"),
                "time": now.strftime("%I:%M:%S %p")
            })

            save_data(data)

            return

        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

    display_board(board)

    print("\n🤝 Match Draw!")

    data = load_data()
    now = datetime.now()

    data["matches"].append({
        "player1": player1,
        "player2": player2,
        "winner": "Draw",
        "day": now.strftime("%A"),
        "date": now.strftime("%d-%m-%Y"),
        "time": now.strftime("%I:%M:%S %p")
    })

    save_data(data)


# ================= MENU =================

while True:

    print("\n===== TIC TAC TOE =====")
    print("1. Play Game")
    print("2. Show Match History")
    print("3. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        play_game()

    elif choice == "2":
        show_history()

    elif choice == "3":
        print("\nGood Bye!")
        break

    else:
        print("Invalid choice.")