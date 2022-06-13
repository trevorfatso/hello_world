def string_column(string_list):
    max_length = len(max(string_list, key=len))
    new_list = []
    
    for i in range(len(string_list)):
        new_list.append([string_list[i]])
        
    for index in range(max_length):
        for string in new_list:
            try:
                print(string[0][index], end=' ')
            except IndexError:
                print(' ', end=' ')
        print()