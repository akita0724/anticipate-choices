from time import time
from json import load, dump
from data.data import SECTION

with open("./data/way2model_1.json", "r") as f:
    modelData = load(f)

startAt = time()

result = {}

for N in range(1, 6):
    rateN = {}
    for section in SECTION:
        keys = modelData[str(N)][section].keys()

        rateSection = {}
        for key in keys:
            rate = [0] * 4
            markov = modelData[str(N)][section][key]
            su = sum(markov)
            rate[0] = markov[0] / su
            rate[1] = (markov[1] / su) + rate[0]
            rate[2] = (markov[2] / su) + rate[1]
            rate[3] = 1

            rateSection[key] = rate

        rateN[section] = rateSection

    result[N] = rateN

endAt = time()
print(f"Process took {endAt - startAt}(s)")

with open("./data/way2model_2.json", "w") as f:
    dump(result, f)
