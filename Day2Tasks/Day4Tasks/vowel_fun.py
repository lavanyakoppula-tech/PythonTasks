def count_v(s):
    return sum(1 for c in s if c in "aeiou")
print(count_v("hello"))
