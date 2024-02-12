from time import time
from json import dump, load
from lib.round import rounding
from lib.score import scoring
from data.data import PROCESS, SECTION
from multiprocessing import Pool
from random import SystemRandom

order = 10 ** 6

rand = SystemRandom()

with open("./data/data.json", "r") as f:
    ansData = load(f)


def generateResultDict(section: str):
    result = {}

    pointPerQ = ansData[section]["P"]
    for _ in range(ansData[section]["qA"] + 1):
        result[rounding(str(pointPerQ * _))] = 0

    return result


def main(section: str):
    _ = 0
    ansDict = generateResultDict(section)
    while _ <= order:
        answer = []
        for q in range(ansData[section]["qA"]):
            answer.append(rand.randint(1, 4))
        score = scoring(section, "".join(list(map(str, answer))))
        ansDict[score] += 1

        _ += 1
    print(f"{section} completed.")
    return {"section": section, "result": ansDict}


if __name__ == "__main__":
    startAt = time()

    pool = Pool(PROCESS)
    result = pool.map(main, SECTION)

    resToWrite = {}

    for res in result:
        resToWrite[res["section"]] = res["result"]

    with open("./data/way1_result.json", "w")as f:
        dump(resToWrite, f)

    endAt = time()
    print(f"Process took {endAt - startAt}(s)")
