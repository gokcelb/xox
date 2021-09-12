X = 'x'
O = 'o'
EMPTY = ' '


class NotEmptyCellException(Exception):
    pass

board = [[EMPTY for _ in range(3)] for _ in range(3)]


def is_full(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False
    return True


def place_input(arr, position, turn):
    i, j = map(int, position.split())

    if arr[i][j] != EMPTY:
        raise NotEmptyCellException

    arr[i][j] = turn


def next_turn(turn):
    if turn == X:
        return O
    return X


def check_horizontal_win(arr, turn):
    for i in range(len(arr)):
        result = 0
        for j in range(len(arr)):
            if arr[i][j] == turn:
                result += 1
        if result == len(arr):
            return True
    return False


def check_vertical_win(arr, turn):
    for j in range(len(arr)):
        result = 0
        for i in range(len(arr)):
            if arr[i][j] == turn:
                result += 1
        if result == len(arr):
            return True
    return False


def check_left_diagonal_win(arr, turn):
    result = 0
    for i in range(len(arr)):
        if arr[i][i] == turn:
            result += 1
    return result == len(arr)


def check_right_diagonal_win(arr, turn):
    result = 0
    for i in range(len(arr)):
        j = len(arr)-i-1
        if arr[i][j] == turn:
            result += 1
    return result == len(arr)


def check_win(arr, turn):
    return check_horizontal_win(arr, turn) or check_vertical_win(
        arr, turn) or check_left_diagonal_win(arr, turn) or check_right_diagonal_win(arr, turn)


def print_board(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            print(arr[i][j], end=" | ")
        print(arr[i][len(arr)-1], end="")
        if i != (len(arr)-1):
            print("\n---------")

    print()


print("sample input: 0 0")
print_board(board)

turn = X

while not is_full(board):
    position = input()
    try:
        place_input(board, position, turn)
        print_board(board)
        if check_win(board, turn):
            print("%s wins" % turn)
            break
        turn = next_turn(turn)
    except NotEmptyCellException as e:
        print("position full")
        print_board(board)
    except:
        print("wrong input")
        print_board(board)