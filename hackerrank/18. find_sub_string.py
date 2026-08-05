'''
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints

Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC

Sample Output
2
'''

def count_substring(string, sub_string):
    
    start = 0
    end = len(sub_string)
    counter = 0
    
    # Loop until the right end of the window exceeds the string's length
    while end <= len(string): 
        # Extract a slice starting at 'start' up to (but not including) index 'end'
        if sub_string == string[start:end]: 
            counter += 1
        start += 1  # Slide the start index one position to the right
        end += 1    # Slide the end index one position to the right
    
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)





