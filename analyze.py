from json import load, dump
from data.data import SECTION
from time import time

# JSONデータを読み込み
with open("./data/data.json", "r") as f:
    ansData = load(f)

# 分析結果を格納する変数
analyzeResult = {}

startAt = time()

# 試験区分ごとに処理を行う
for section in SECTION:
    res = [0] * 4
    # 1回分の解答一覧
    for d in ansData[section]["sD"]:
        # 解答の数値を認識
        for ans in d:
            res[int(ans) - 1] += 1

    analyzeResult[section] = res

endAt = time()
print(f"Process took {endAt - startAt}(s)")

with open("./data/analyze.json", "w") as f:
    dump(analyzeResult, f)
