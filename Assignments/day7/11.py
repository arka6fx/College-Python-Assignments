
from functools import reduce
l1 = [1, 2, 3, 4, 5, 6]
f = lambda x, y: x + y
r = reduce(f, l1)
print(r)  # Output: 21

# Explanation (Addition):
# [1, 2, 3, 4, 5, 6]
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
# 15 + 6 = 21