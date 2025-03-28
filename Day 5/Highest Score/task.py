from statistics import median

# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
student_scores = [8, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

total_score = sum(student_scores)
print(total_score)
average_score = total_score / len(student_scores)
print(average_score)

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print(high_score)