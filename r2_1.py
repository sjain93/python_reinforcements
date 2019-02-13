def grade_calc(percent):
    if percent >= 90:
        return 'A+'
    elif percent >= 85:
        return 'A'
    elif percent >= 80:
        return 'A'
    elif percent >= 77:
        return 'B+'
    elif percent >= 73:
        return 'B'
    elif percent >= 70:
        return 'B-'
    elif percent >= 65:
        return 'C+'
    elif percent >= 60:
        return 'C'
    elif percent >= 55:
        return 'C-'
    elif percent >= 50:
        return 'D'
    else:
        return 'F'
    
print("Enter the percent grade from 1-100")
percent = float(input())
print("Your letter grade is {}".format(grade_calc(percent)))
