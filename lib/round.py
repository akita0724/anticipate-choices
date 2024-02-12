from decimal import *


def rounding(num: float | int) -> str:
    """_
    小数点第二位で四捨五入を行う関数
    """
    d = Decimal(str(num))
    d = d.quantize(Decimal(".1"), rounding=ROUND_HALF_UP)
    return str(d)
