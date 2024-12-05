gyo = int(input("行数を入力してください:"))
retu = int(input("列数を入力してください:"))
for i in range(1, gyo + 1):
    for j in range(1, retu + 1):
        print(f"{j:2}×{i:2} =, {i * j:2} |", end=" ")
    print("")
