import random
import time

def display_board(board):
    print("\n".join(" ".join(row) for row in board))

def create_board(size):
    cards = [chr(65 + i) for i in range(size * size // 2)] * 2
    random.shuffle(cards)
    board = [cards[i:i + size] for i in range(0, len(cards), size)]
    return board

def hide_board(size):
    return [["*" for _ in range(size)] for _ in range(size)]

def get_coordinates(size):
    while True:
        try:
            coords = input("Enter the coordinates (row, col) separated by a space: ")
            x, y = map(int, coords.split())
            if 0 <= x < size and 0 <= y < size:
                return x, y
            else:
                print("Coordinates are out of bounds. Try again.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")


def memory_puzzle(size=4, time_limit=60):
    print("Welcome to the Memory Puzzle Game!")
    board = create_board(size)
    hidden_board = hide_board(size)
    matched = set()
    start_time = time.time()

    while len(matched) < size * size:
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print("Time's up! You lose. Better luck next time.")
            return

        print("\nTime Remaining: {:.0f}s".format(time_limit - elapsed_time))
        display_board(hidden_board)

        print("\nSelect your first card:")
        x1, y1 = get_coordinates(size)
        if (x1, y1) in matched:
            print("This card is already matched. Choose another one.")
            continue

        print("\nSelect your second card:")
        x2, y2 = get_coordinates(size)
        if (x2, y2) in matched or (x1 == x2 and y1 == y2):
            print("Invalid selection. Try again.")
            continue

        hidden_board[x1][y1] = board[x1][y1]
        hidden_board[x2][y2] = board[x2][y2]
        display_board(hidden_board)

        if board[x1][y1] == board[x2][y2]:
            print("You found a match!")
            matched.update([(x1, y1), (x2, y2)])
        else:
            print("Not a match. Try again.")
            time.sleep(2)
            hidden_board[x1][y1] = "*"
            hidden_board[x2][y2] = "*"

    print("Congratulations! You matched all pairs!")

def main():
    memory_puzzle()

if __name__ == "__main__":
    main()