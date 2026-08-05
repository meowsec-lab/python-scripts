
def split_and_join(line):
    i = line.split(" ") # the input string will be splitted here
  # "red apple" input is ['red', 'apple'] after split
  
    j = "-".join(i) # join fuction concatenate the splitted string
  # here the input will join with -  between them
    
    return j

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
