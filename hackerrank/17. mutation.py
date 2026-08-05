# List = mutable, that means we can change a value from list
# Tuple = immutable, that means we cannot change value from a tuple
# String = we cannot change a value from inside string directly


def mutate_string(string, position, character):
    
    my_list = list(string) # convert the string into list so that it can be edited
    my_list[position] = character # now from the list, any character of any position can be changed
    
    return ''.join(my_list) # now join the list and make it a full string here

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
