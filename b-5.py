i = input("データを入力してください >")
j = i.split(" ")
# 実行結果
# データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
# 合計値: 54
sum_i = 0
for num in j:
    sum_i += int(num)
print(sum_i)

# 最大値: 21
max_i = 0
for num in j:
    if max_i < int(num):
        max_i = int(num)
print(max_i)

# 最小値: 1
min_i = int(num[0])
for num in j:
    if min_i > int(num):
        min_i = int(num)
print(min_i)
# 平均値: 6
sum_i = 0
for num in j:
    sum_i += int(num)
ave_i = sum_i // len(j)
print(ave_i)
