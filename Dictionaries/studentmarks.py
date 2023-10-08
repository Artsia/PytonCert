# Finding student marks as a percentage, HR

if __name__ == '__main__':
    n = int(input())
    maxLength = 3
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    # Check if the student exists in the dictionary
    if query_name in student_marks:
        
        # retrieve array of student marks based on student_name
        scores = student_marks[query_name]
        
        # hardcoded maxlength since a constraint but can be len(scores)
        scoreAvg = sum(scores)/maxLength
        
        # format by 2 decimal places after decimal
        print("%.2f" % scoreAvg)
