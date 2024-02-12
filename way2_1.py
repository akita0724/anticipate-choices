from json import load, dump
from time import time
from collections import deque
from data.data import PROCESS, SECTION

with open("./data/data.json", "r") as f:
    ansData = load(f)

startAt = time()


def mkModel(N: int, answers: list[list[str]]):
    model = {}

    for answer in answers:
        q = deque([], N)
        q.append("[BOS]")
        for next in answer[: -1]:
            key = "".join(list(q))

            if key not in model:
                model[key] = [0]*4

            model[key][int(next) - 1] += 1

            q.append(next)

    return model


modelData = {}

for N in range(1, 6):
    modelN = {}
    for section in SECTION:
        model = mkModel(N, ansData[section]["sD"])
        modelN[section] = model
    modelData[str(N)] = modelN

endAt = time()
print(f"Process took {endAt - startAt}(s)")

with open("./data/way2model_1.json", "w") as f:
    dump(modelData, f)
