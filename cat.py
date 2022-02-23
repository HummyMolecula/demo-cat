class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name = "", age = 1, happy = False):
        self.name = name
        self.age = age
        self.isHappy = happy

cat1 = Cat()
cat1.set_data("Barsik", 3, True)

cat2 = Cat()
cat2.set_data("Schopen", 2)

print("First cat:", cat1.name)
print("Second cat:", cat2.name)
