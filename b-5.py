i = input("データを入力してください >")
j = i.split(" ")


# 実行結果
# データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
# 合計値: 54
def sum_i(i):
    sum_i = 0
    for num in j:
        sum_i += int(num)
    return sum_i


# 最大値: 21
def max_i(i):
    max_i = 0
    for num in j:
        if max_i < int(num):
            max_i = int(num)
    return max_i


# 最小値: 1
def min_i(i):
    min_i = int(num[0])
    for num in j:
        if min_i > int(num):
            min_i = int(num)
    return min_i


# 平均値: 6
def ave_i(i):
    for num in j:
        sum_i += int(num)
    ave_i = sum_i // len(j)
    return ave_i
