class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name = "", age = 1, happy = False):
        self.set_data(name, age, happy)
        self.get_data()

    def set_data(self, name = "", age = 1, happy = False):
        self.name = name
        self.age = age
        self.isHappy = happy

    def get_data(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Happy?:", self.isHappy)

cat1 = Cat("Barsik", 3, True)
cat2 = Cat("Schopen", 2)
