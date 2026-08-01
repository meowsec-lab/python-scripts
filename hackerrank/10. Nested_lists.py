'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
'''


def score_sorting(student_score):
    # make a separate list of score only
    scores = []
    for i in student_score:
        scores.append(i[1])
        
    # sort and de-duplicate the student scores
    sorted_scores = sorted(set(scores))
    
    # save the second lowest
    second_low_score = sorted_scores[1]
    
    # find all the second lowest grader names
    name_of_seond_low = []
    for k in student_score:
        if k[1] == second_low_score:
            name_of_seond_low.append(k[0]) 
    
    # now sort the names
    name_of_seond_low = sorted(name_of_seond_low)
    
    # print the sorted names
    for name in name_of_seond_low:
        print(name)

if __name__ == '__main__':
    student_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_score.append([name, score])
    
    # call the function
    score_sorting(student_score)
