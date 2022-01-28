from typing import List


def countStudents(students: List[int], sandwiches: List[int]) -> int:
    student_map = {0: 0, 1: 0}

    for i in range(len(students)):
        student_map[students[i]] += 1

    while len(sandwiches) > 0:
        if student_map[sandwiches[0]]:
            student_map[sandwiches[0]] -= 1
            sandwiches.pop(0)
        else:
            break

    return len(sandwiches)


students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]

print(countStudents(students, sandwiches))
