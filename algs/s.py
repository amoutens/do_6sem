def s_calculate(x, students):
    result = 0
    for student_id in range(len(x[0])):
        for discipline_ids in x:
            if discipline_ids[student_id] == 1:
                result += students[student_id]
                break
    return result