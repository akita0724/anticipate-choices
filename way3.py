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


def main(arg: list):
    N = arg[0]
    section = arg[1]

    model = modelData[str(N)][section]
    ansDict = generateResultDict(section)

    _ = 0
    while _ < order:
        firstAns = int(ansData[section]["aD"][0])
        answer = [firstAns]
        q = deque([], N)

        q.append("[BOS]")
        # 初期解を与える
        q.append(str(firstAns))

        # 初期解を与えるため異なる
        for a in range(ansData[section]["qA"] - 2):

            markov = "".join(list(q))

            if markov not in model:
                nextA = rand.randint(1, 4)
            else:
                nextA = next(index for index, prob in enumerate(
                    model[markov]) if rand.random() < prob) + 1

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

    with open("./data/way3_result.json", "w")as f:
        dump(resToWrite, f)

    endAt = time()

    print(f"Process took {endAt - startAt}(s)")
