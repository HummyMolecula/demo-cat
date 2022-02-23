class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name = "", age = 1, happy = False):
        self.name = name
        self.age = age
        self.isHappy = happy

cat1 = Cat()
cat1.name = "Barsik"
cat1.age = 3
cat1.isHappy = True

cat2 = Cat()
cat2.name = "Shopen"
cat2.age = 4
cat2.isHappy = True

print("First cat:", cat1.name)
print("Second cat:", cat2.name)
