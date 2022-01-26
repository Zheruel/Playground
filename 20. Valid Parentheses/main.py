def isValid(s: str) -> bool:
    stack = []
    identifier_dict = {")": "(", "]": "[", "}": "{"}

    for l in s:
        if l in identifier_dict:
            if stack and identifier_dict[l] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(l)

    if not stack:
        return True
    else:
        return False


s = "()[]{}"
print(isValid(s))
