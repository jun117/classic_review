class Customer:
    def __init__(self, first_name, family_name,age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return (f"{self.first_name} {self.family_name}")


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)

# C-1
print(ken.first_name)  # "Ken Tanaka" という値を返す
print(tom.full_name())  # "Tom Ford" という値を返す

# C-2
print(ken.age)
print(tom.age)
print(ieyasu.age)
