class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return (f"{self.first_name} {self.family_name}")

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif 3 < self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif 65 <= self.age < 75:
            return 1200
        else:
            return 500

    def info_csv(self):
        return (f"{self.first_name} {self.family_name},{self.age},{self.entry_fee()}")

    def tab(self):
        return (f"{self.first_name} {self.family_name}\t{self.age}\t{self.entry_fee()}")

    def pipe(self):
        return (f"{self.first_name} {self.family_name}|{self.age}|{self.entry_fee()}")


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
jun = Customer(first_name="Jun", family_name="Onuma", age=3)
kin = Customer(first_name="Kin", family_name="Gin", age=100)

# C-1
print(ken.full_name())  # "Ken Tanaka" という値を返す
print(tom.full_name())  # "Tom Ford" という値を返す

# C-2
print(ken.age)
print(tom.age)
print(ieyasu.age)

# C-3
print(f"子供料金は（20歳未満）:{ken.entry_fee()}円")
print(f"おとな料金（20歳以上65歳未満）：{tom.entry_fee()}円")
print(f"シニア料金（65歳以上）：{ieyasu.entry_fee()}円")

# C-4
print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())

# C-5
print(jun.entry_fee())

# C-6
print(kin.entry_fee())

# C-7
print(ken.tab())
print(tom.tab())
print(ieyasu.tab())

# C-8
print(ken.pipe())
print(tom.pipe())
print(ieyasu.pipe())
