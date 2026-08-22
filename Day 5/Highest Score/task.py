student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

maximum = 0
for score in student_scores:
    if score > maximum:
        maximum = score
print(maximum)

exam_score = sum(student_scores)
print(exam_score)


sum = 0
for score in student_scores:
    sum += score
print(sum)

sum = 0
for number in range(1, 101):
    sum += number
print(sum)




