# ここにコードを記述
def dice():
    import random

    saikoro = ["1", "2", "3", "4", "5", "6"]
    idx = random.randint(0, 5)
    result = saikoro[idx]
    return result


print(dice())  # 1から6の整数をランダムに出力する
