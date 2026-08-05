'''
Task
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
'''

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

  # convert list to tuple using tuple()
  # generate hash of the tuple using hash()
  
    print(hash(tuple(integer_list)))
