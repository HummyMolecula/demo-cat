class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self):
        pass

    def set_data(self, name = "", age = 1, happy = False):
        self.name = name
        self.age = age
        self.isHappy = happy

    def get_data(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Happy?:", self.isHappy)

cat1 = Cat()
cat1.set_data("Barsik", 3, True)

cat2 = Cat()
cat2.set_data("Schopen", 2)

print("First cat:")
cat1.get_data()
print("Second cat:")
cat2.get_data()
