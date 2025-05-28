def reverseWord(word):
    stack = []
    reversed = ''
    for char in word:
        stack.append(char)
    while stack:
        reversed += stack.pop()
    return reversed

w = "university"
r = reverseWord(w)
print(f"Before: {w}")
print(f"After: {r}")