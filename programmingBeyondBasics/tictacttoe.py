"""
- game can be represented as 2x2 grid
- each player should be able to select a position
    - check if its already occupied
    - if yes, return
    - if no, mark position
    - after marking, determine if winner
        - this can be determined if same shape matches following criteria
            - [0,0] -> [0,1] -> [0,2]
            - [0,0] -> [1, 0] -> [2,0]
            - [0,0] -> [1,1] -> [2,2]

            - pattern here is same diagnal, same row all columns, same column all rows
"""

grid = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

winning_pos = [
    # diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
    # Vertical
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # Horizontal
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
]
def switch_player(shape):
    return 'O' if shape == 'X' else 'X'

def check_winner(grid, shape):
    # check if shape is present in either row of winning_pos
    for row in winning_pos:
        if all(grid[x][y] == shape for x, y in row):
            print(f'{shape} is the winner')
            return True
    return False        

def tic_tac_toe(grid):
    shape = 'X'
    game_start = True
    while game_start:
        row = int(input('Enter row position (0-2): '))
        column = int(input('Enter column position (0-2): '))

        if grid[row][column] != '':
            print('pos already taken')
            continue

        grid[row][column] = shape
        if check_winner(grid, shape):
            game_start = False
        else:
            shape = switch_player(shape)

        print(grid)

    print('Game over!')

if __name__ == '__main__':
    tic_tac_toe(grid)



