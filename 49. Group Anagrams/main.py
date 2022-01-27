from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    str_dict = defaultdict(list)

    for str in strs:
        tracker = [0] * 26

        for c in str:
            tracker[ord(c) - ord("a")] += 1

        str_dict[tuple(tracker)].append(str)

    return str_dict.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
