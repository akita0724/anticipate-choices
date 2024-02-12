from random import SystemRandom
from time import time

order = 10 ** 6

rand = SystemRandom()

_ = 0

result = [0] * 20

startAt = time()

while _ < order:

    result[int(rand.random() // 0.05)] += 1
    _ += 1

print(result)

endAt = time()
print(f"Process took {endAt - startAt}(s)")
