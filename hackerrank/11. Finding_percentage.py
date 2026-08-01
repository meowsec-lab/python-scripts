'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example

The query_name is 'beta'. beta's average score is .


'''

def average_score(marks, query_name):
  
  # access key only, using marks.keys()
  # access value only, using marks.values()
  # access both value, use items()
  
    for key, value in marks.items():
        if key == query_name:
            average = sum(value) / len(value)
    print(f"{average:.2f}") 
    

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    average_score(student_marks, query_name)
