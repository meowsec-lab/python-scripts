'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
'''

if __name__ == '__main__':
    N = int(input())
    
    my_list = []
    
    for i in range(N):
        uInput = input().split()
        
        if uInput[0] == 'insert':
            my_list.insert(int(uInput[1]), int(uInput[2]))
        elif uInput[0] == 'print':
            print(my_list)
        elif uInput[0] == 'remove':
            my_list.remove(int(uInput[1]))
        elif uInput[0] == 'append':
            my_list.append(int(uInput[1]))
        elif uInput[0] == 'sort':
            my_list.sort()
        elif uInput[0] == 'pop':
            my_list.pop()
        elif uInput[0] == 'reverse':
            my_list.reverse()
            
        
