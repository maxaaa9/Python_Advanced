def palindrome(name, index):
    if index == len(name) // 2:
        return f"{name} is a palindrome"

    if name[index] != name[-index-1]:
        return f"{name} is not a palindrome"

    return palindrome(name, index + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))


