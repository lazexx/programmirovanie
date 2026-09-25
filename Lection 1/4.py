from collections import Counter

a = input().lower()
print(Counter(a).most_common(3))