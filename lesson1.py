
class Student:
    happy = 0
    tiredness = 0
    sleep = 0
    force = 0
    fantasy = 0
    money = 0
    life = 0
    
    def __init__(self, Happy, Tiredness, Sleep, Force, Fantasy, Money, Life):
        self.happy = Happy
        self.tiredness = Tiredness
        self.sleep = Sleep
        self.force = Force
        self.fantasy = Fantasy
        self.money = Money
        self.life = Life

    def get_study(self):
        self.happy -= 10
        self.tiredness -= 10
        self.sleep += 10
        self.force -= 10
        self.fantasy -= 10
        self.life += 90
    def get_relax(self):
        self.tiredness -= 10
        self.happy += 10
        self.force += 10
        self.money -= 10
        self.life += 90
    def get_sleep(self):
        self.tiredness -= 10
        self.happy += 10
        self.force += 10
        self.life += 90
        self.sleep -= 10
    def get_work(self):
        self.tiredness += 10
        self.sleep -= 10
        self.happy -= 10
        self.force += 10
        self.money += 100
        self.life += 90



student1 = Student(50, 50, 100, 100, 150, 100, 1)
student2 = Student(50, 50, 100, 100, 150, 100, 1)
student1.get_study()
student1.get_sleep()
student1.get_relax()
student1.get_work()
student2.get_study()
student2.get_work()
student2.get_relax()
student2.get_sleep()
print(student1.happy, student1.tiredness, student1.sleep, student1.force, student1.fantasy, student1.money, student1.life)
print(student2.happy, student2.tiredness, student2.sleep, student2.force, student2.fantasy, student2.money, student2.life)