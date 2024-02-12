from json import load
from lib.round import rounding


def scoring(section: str, answer: str) -> str:
    """
    採点を行う関数

    - section: 試験区分
    - answer:  答案を連結したもの
    """

    # 解答例データを読み込み
    with open("./data/data.json", "r") as f:
        ansDataALL = load(f)

    # 指定の区分のみ読み込み
    ansData = ansDataALL[section]

    # 点数を初期化
    score = 0

    # 配点を読み込み
    scorePerQ = ansData["P"]

    # 採点を実施
    for ans, cor in zip(ansData["aD"], answer):
        score += 1 if ans == cor else 0

    # 採点結果(得点)を求める
    # AM1で100点を超えうるためmin()で上に蓋をする
    score = min(100, score * scorePerQ)

    # 浮動小数点表記の特性上誤差が生じるので小数点第2位以下を四捨五入して返す
    return rounding(score)
