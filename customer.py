# 下記の雛形を利用して、各問のコードが期待通り動作するようなCustomerクラスを実装してください


from inspect import AGEN_CLOSED


class Customer:
    # 各問のコードが期待通り動作するように実装
    #コンストラクタ(初期化メソッド)
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age
    
    # C−1メソッド
    def full_name(self):
        return f"{self.first_name} {self.family_name}"
    
    # C-2メソッド
    def custmoer_age(self):
        return f"{self.age}"
    
    # C-3・C-5メソッド
    def entry_fee(self):
        if self.age  <= 3:
            entry_fee = 0
        elif self.age <20:
            entry_fee = 1000
        elif self.age >=20 and self.age <= 65:
            entry_fee = 1500
        else:
            entry_fee = 1200
        return entry_fee
    
    # C−4メソッド
    def info_csv(self):
        return f"{self.full_name()}",{self.age},{self.entry_fee()}

     # C-6: 75歳以上500円
    def entry_fee_c6(self):
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        elif self.age < 75:
            return 1200
        else:
            return 500

    # C-7 タブ区切りのCSV
    def info_csv(self):
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}\t"

    # C-8 「|」(パイプ)区切り
    def v_separate(self):
        return f"{self.full_name()} | {self.age} | {self.entry_fee()}"

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)


# C-1 出力(フルネームで取得できる)
print("【C-1出力】")
print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力


# C-2 出力(年齢という概念の追加)
print("【C-2出力】")
print(ken.age)  # 15 という値を出力
print(tom.age) # 57 という値を出力
print(ieyasu.age) # 75 という値を出力


# C-3 年令に応じた適切な入場料(entry_fee)を計算できる

print("【C-3出力】")
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力


# C-4 単一の顧客情報をCSV形式で取得できる
print("【C-4出力】")
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力



# 応用問題
# Customerクラスの実装だけでなく、仕様の理解やどのようにクラスを利用するのかも含めて考えてください

# C-5 3歳以下の入場料の無料化

print("【C-5出力】")
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
print(michelle.entry_fee())  # 0 という値を出力


# C-6 75歳以上の入場料金は500円にしてください

print("【C-6出力】")
print(ieyasu.entry_fee_c6())

# C-7 単一顧客の情報取得形式の追加その1
# 単一顧客の情報取得をタブ区切りにも対応させてください


print("【C-7出力】")
print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())
print(michelle.info_csv())


# C-8 単一顧客の情報取得形式の追加その2
# 単一顧客の情報取得を「|」(パイプ)区切りにも対応させてください


print("【C-8出力】")
print(ken.v_separate())
print(tom.v_separate())
print(ieyasu.v_separate())
print(michelle.v_separate())