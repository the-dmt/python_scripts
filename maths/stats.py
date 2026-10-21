import math
import statistics as st

nums = [30, 10, 60, 20, 10, 40]
nums.sort()

def mean(x):
    return sum(x) / len(x)

def median(x):
    if len(x) % 2 == 1:
        return x[len(x) // 2]
    else:
        return (x[len(x) // 2] + x[len(x) // 2 - 1]) / 2

def mode(x):
    return max(set(x), key=x.count)

print(st.mean(nums))
print(st.harmonic_mean(nums))
