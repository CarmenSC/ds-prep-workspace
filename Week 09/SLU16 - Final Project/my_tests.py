from mines import MinesweeperGame

game = MinesweeperGame(3, 3)
print(game.get_surrounding_cells(1, 1))


for new_x, new_y in game.get_surrounding_cells(1, 1):
    game.click(new_x,new_y)




'''
surrounding_cells = game.get_surrounding_cells(1, 1)
print(surrounding_cells)

number_of_mines = 0

for i in surrounding_cells:
    x, y = i[0], i[1]
    if game.check_if_mine(x,y):
        number_of_mines += 1
print(number_of_mines)
'''


'''
number_of_mines = 0
for i in surrounding_cells:
    if game.check_if_mine(i):
        number_of_mines += 1
        return number_of_mines
'''