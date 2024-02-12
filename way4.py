from collections import deque
from time import time
from json import load, dump
from multiprocessing import Pool
from data.data import PROCESS, SECTION
from random import SystemRandom
from lib.score import scoring
from way1 import generateResultDict

rand = SystemRandom()

order = 10 ** 6

with open("./data/way2model_2.json", "r") as f:
    modelData = load(f)

with open("./data/data.json", "r") as f:
    ansData = load(f)


def sub(N: int, markov: str, section: str) -> str:
    model = modelData[str(N)][section]
    if not markov in model:
        return sub(N - 1, markov[1:], section)
    else:
        random = rand.random()

        for nex, i in enumerate(model[markov]):
            if random <= i:
                return str(nex + 1)


def main(arg: list):
    N = arg[0]
    section = arg[1]

    ansDict = generateResultDict(section)

    _ = 0
    while _ <= order:
        answer = []
        q = deque([], N)
        q.append("[BOS]")

        for a in range(ansData[section]["qA"] - 1):

            markov = "".join(list(q))

            nextA = sub(N, markov, section)

            q.append(str(nextA))

            answer.append(nextA)

        score = scoring(section, "".join(list(map(str, answer))))

        ansDict[score] += 1

        _ += 1

    print(f"{section} - {N} completed.")
    return {"section": section, "N": N, "result": ansDict}


if __name__ == "__main__":

    arg = []

    for section in SECTION:
        for N in range(1, 6):
            arg.append([N, section])

    startAt = time()

    pool = Pool(PROCESS)
    result = pool.map(main, arg)

    resToWrite = {}

    for res in result:
        section = res["section"]
        if section not in resToWrite:
            resToWrite[section] = {}
        resToWrite[section][res["N"]] = res["result"]

    with open("./data/way4_result.json", "w")as f:
        dump(resToWrite, f)

    endAt = time()

    print(f"Process took {endAt - startAt}(s)")
