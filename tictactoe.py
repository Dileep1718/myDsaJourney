def table(x_moves, o_moves):
    zero = 'X' if x_moves[0] else ('O' if o_moves[0] else 0)
    one = 'X' if x_moves[1] else ('O' if o_moves[1] else 1)
    two = 'X' if x_moves[2] else ('O' if o_moves[2] else 2)
    three = 'X' if x_moves[3] else ('O' if o_moves[3] else 3)
    four = 'X' if x_moves[4] else ('O' if o_moves[4] else 4)
    five = 'X' if x_moves[5] else ('O' if o_moves[5] else 5)
    six = 'X' if x_moves[6] else ('O' if o_moves[6] else 6)
    seven = 'X' if x_moves[7] else ('O' if o_moves[7] else 7)
    eight = 'X' if x_moves[8] else ('O' if o_moves[8] else 8)

    print(f" {zero} | {one} | {two} ")
    print("------------")
    print(f" {three} | {four} | {five} ")
    print("------------")
    print(f" {six} | {seven} | {eight} ")


def check(x_moves, o_moves):
    winning = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 4, 8], [2, 4, 6], [0, 3, 6],
        [1, 4, 7], [2, 5, 8]
    ]
    for win in winning:
        if (x_moves[win[0]] + x_moves[win[1]] + x_moves[win[2]]) == 3:
            print("X won")
            return 1
        if (o_moves[win[0]] + o_moves[win[1]] + o_moves[win[2]]) == 3:
            print("O won")
            return 0
    return -1


if __name__ == "__main__":
    x_moves = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    o_moves = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    chance = 1
    while True:
        table(x_moves, o_moves)
        if chance == 1:
            print("It's X's turn")
            value = int(input("Please enter a value (0-8): "))
        else:
            print("It's O's turn")
            value = int(input("Please enter a value (0-8): "))

        # Prevent overwriting moves
        if x_moves[value] == 1 or o_moves[value] == 1:
            print("Cell already taken. Try again.")
            continue

        # Update the moves
        if chance == 1:
            x_moves[value] = 1
        else:
            o_moves[value] = 1

        # Check for a winner
        win_check = check(x_moves, o_moves)
        if win_check != -1:
            table(x_moves, o_moves)
            break

        # Check for a draw
        if all(x_moves[i] or o_moves[i] for i in range(9)):
            table(x_moves, o_moves)
            print("It's a draw!")
            break

        # Alternate the chance
        chance = 1 - chance
