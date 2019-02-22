class Robot:
    def __init__(self, new_name):
        self.name = new_name
        self.life = 10

    def talk(self):
        print("My name is {} and I have {} life".format(self.name, self.life))

robot1 = Robot("Sally")
print(robot1)

print(robot1.name)
print(robot1.life)

robot2 = Robot("Steve")

robot1.talk()
