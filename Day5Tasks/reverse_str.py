def rev(s):
    if len(s) == 0:
        return ""
    return s[-1] + rev(s[:-1])

print(rev("hello"))
