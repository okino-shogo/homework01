import random

N = int(input("サイコロの面の数は?:"))
M = int(input("何回振りますか?:"))
# 実行結果
# サイコロの面の数は?: 8
# 何回振りますか?: 20
# [6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]

result = []
for kaisu in range(M):
    num = random.randint(1, N)
    result.append(num)
print(result)
