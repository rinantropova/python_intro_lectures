# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


# desired_grade = 5
initial_grades = [2, 3, 3, 5, 3]


def replace_grades(grades):
    max_grade = max(grades)
    min_grade = 1
    return [min_grade if grade == max_grade else grade for grade in grades]


result_grades = replace_grades(initial_grades)
print(*result_grades)


# Recursion:
def replace_grades_recur(grades, max_grade=None, min_grade=1):
    if len(grades) == 0:
        return grades
    # min_grade = 1
    if max_grade is None:
        max_grade = max(grades)
    updated_grades = grades.copy()

    if updated_grades[0] == max_grade:
        updated_grades[0] = min_grade
    return [updated_grades[0]] + replace_grades_recur(updated_grades[1:], max_grade, min_grade)


print(*replace_grades_recur(initial_grades))

# Seminar's solution:
min_grade = min(initial_grades)
max_grade = max(initial_grades)
new_grades = []
for grade in initial_grades:
    if grade == max_grade:
        new_grades.append(min_grade)
    else:
        new_grades.append(grade)
print(*new_grades)

# Comprehension:
print([min_grade if grade == max_grade else grade for grade in initial_grades])


#Recursion
def update_grades(initial_grades, grades2=[], min_grade = min(initial_grades), max_grade = max(initial_grades)):
    if len(initial_grades) == 0:
        return grades2
    if initial_grades[0] == max_grade:
        grades2.append(min_grade)
    else:
        grades2.append(initial_grades[0])
    return update_grades(initial_grades[1:], grades2)

print(update_grades(initial_grades))
