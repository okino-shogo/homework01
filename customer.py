class Customer:
    # init 初期化 クラスの中の関数のことをメソットという
    def __init__(self, first_name, family_name, age):
        # ↓属性
        self.first_name = first_name
        self.family_name = family_name
        # C-2
        self.age = age

    # C-1
    def full_name(self):
        return "{} {}".format(self.first_name, self.family_name)

    # C-3
    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        else:
            return 1200

    # C-4
    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"


# インスタンス化
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)

# C-1
print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力

# C-2
print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力

# C-3
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力

# C-4
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力
