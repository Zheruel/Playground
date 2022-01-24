def isAnagram(s: str, t: str) -> bool:
    if len(s) == len(t):
        s_dict = {}

        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1

        for letter in t:
            if letter in s_dict:
                s_dict[letter] -= 1
            else:
                return False

        for value in s_dict.values():
            if value:
                return False

        return True

    return False


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
