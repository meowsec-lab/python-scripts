'''
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  

'''

def swap_case(s):
    
    new_list = []
    
    for i in s:
      # check if the character is alpabet with isalpha()
        if i.isalpha():
            if i.islower(): # is the character is lower
                new_list.append(i.upper())
            else:
                new_list.append(i.lower())       
        else:
            new_list.append(i)
    
  # You cannot return the list because it is full of characters
  # convert the list to string using join() using an empty string at first
    return ''.join(new_list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
