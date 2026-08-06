'''
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string, .
The second line contains the width, .


Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

def wrap(string, max_width):
  # Run the loop to keep checking the entire string
    for i in range(0, len(string)+1, max_width): # range(start, end, steps)
        chunk = string[i:i + max_width] # string is immutable. But we can read a chunk without converting it to list. Editing string will require to convert it to list at first
        if len(chunk) == max_width:
            print(chunk)
        else:
            return chunk # return rest of the string that is left over and do not match with max_width

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
