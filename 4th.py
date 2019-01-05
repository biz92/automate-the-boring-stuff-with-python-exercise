my_list = ['peaches', 'tomatoes', 'coconut', 'apple', 'cat']

my_str = ' '

for i in range(len(my_list) - 1):
    my_list[i]
    my_str += my_list[i] + ","

print(my_str + 'and ' + my_list[-1] )
