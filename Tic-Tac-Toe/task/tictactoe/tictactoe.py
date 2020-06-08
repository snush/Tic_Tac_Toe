def print_field(field):
    print("---------")
    for i in range(3):
        print("| {} {} {} |".format(field[i][0], field[i][1], field[i][2]))
    print("---------")


def check(cell1, cell2, cell3):
    return cell1 == cell2 == cell3 != " "


def check_row(field, cell):
    for i in range(3):
        if check(field[i][0], field[i][1], field[i][2]) and field[i][0] == cell:
            return True
    return False


def check_columns(field, cell):
    for j in range(3):
        if check(field[0][j], field[1][j], field[2][j]) and field[0][j] == cell:
            return True
    return False


def check_diagonal(field, cell):
    return (check(field[0][0], field[1][1], field[2][2]) and field[0][0] == cell) or (
            check(field[0][2], field[1][1], field[2][0]) and field[1][1] == cell)


tic_tac_toe = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print_field(tic_tac_toe)
count = 0

while count != 9:
    coordinates = [i for i in input("Enter the coordinates: >  ").split()]

    if coordinates[0].isdigit() and coordinates[1].isdigit():
        column = int(coordinates[0]) - 1
        row = int(coordinates[1]) - 1

        if 0 <= row <= 2 and 0 <= column <= 2:
            if row != 1:
                row = 0 if row == 2 else 2

            if tic_tac_toe[row][column] == " ":

                if count % 2 == 0:
                    tic_tac_toe[row][column] = "X"
                else:
                    tic_tac_toe[row][column] = "O"
                print_field(tic_tac_toe)
                count += 1

                win_X = check_row(tic_tac_toe, "X") or check_columns(tic_tac_toe, "X") or check_diagonal(tic_tac_toe, "X")
                win_O = check_row(tic_tac_toe, "O") or check_columns(tic_tac_toe, "O") or check_diagonal(tic_tac_toe, "O")

                if win_X:
                    print("X wins")
                    break
                elif win_O:
                    print("O wins")
                    break
                elif count == 9:
                    print("Draw")

            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")