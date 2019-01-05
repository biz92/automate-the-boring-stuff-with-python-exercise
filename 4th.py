my_list = ['peaches', 'tomatoes', 'coconut', 'apple', 'cat']

my_str = ' '

for i in range(len(my_list) - 1):
    my_list[i]
    my_str += my_list[i] + ","

print(my_str + 'and ' + my_list[-1] )


## Picture

grid = [['.','.','.','.','.','.'],
        ['.','O','O','.','.','.'],
        ['O','O','O','O','.','.'],
        ['O','O','O','O','O','.'],
        ['.','O','O','O','O','O'],
        ['O','O','O','O','O','.'],
        ['O','O','O','O','.','.'],
        ['.','O','O','.','.','.'],
        ['.','.','.','.','.','.']]

# print(grid[1][1]) # missed in a book?!

for i in range(6):
    for j in range(9):
        print(grid[j][i], end=' ')
    print(' ')
