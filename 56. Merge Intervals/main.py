from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    output = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = output[-1][1]

        if start <= last_end:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start, end])

    return output


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))
