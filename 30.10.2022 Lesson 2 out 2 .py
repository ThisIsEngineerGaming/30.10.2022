import random
class Human:
    def __init__(self, name="Human", job = None, home = None, car = None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.satiety = 50
        self.gladness = 50
    def get_home(self):
        self.home = Home()
    def get_car(self):
        self.car = Car(brand_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
              self.satiety = 100
              return
            self.satiety += 5
            self.home.food -= 5


    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
               self.shopping("fuel")
               return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4



    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("Time to buy dinosaurs turned into black syrup, aka petrol...")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Time to buy human fuel, Dinosaur chicken nuggies...")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Oh boy i bought some funny blue powder from that New Mexican dealer on the US Mexico border")
            self.gladness += 10
            self.money -= 15
            self.satiety += 2

    def chill(self):
        self.gladness += 10
        self.home.mess += 10

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
    def days_indexes(self):
        pass
    def is_alive(self):
        pass
    def live(self):
        pass
class Car:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_of_car[self.brand]["fuel"]
        self.strength = brand_of_car[self.brand]["strength"]
        self.consumption = brand_of_car[self.brand]["consumption"]
    def drive(self):
        if self.strength > 0 and self.fuel > self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car broke. You feel a piece of your soul cracking away and also like 5000$")
            return False
class Home:
    def __init__(self):
        self.mess = 0
        self.food = 0
class Job:
    def __init_(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["Salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]




job_list = {"Java": {"Salary": 50, "gladness_less" : 10},
            "Python": {"Salary": 35, "gladness_less" : 3},
            "C++": {"Salary": 75, "gladness_less" : 25},
            "HTML": {"Salary": 45, "gladness_less" : 1},}





brand_of_car={"Voltswagen Das Auto":{"fuel": 100, "strength": 100, "consumption": 6},
              "Mercedes":{"fuel": 69, "strength": 42, "consumption": 13},
              "Volga":{"fuel": 20, "strength": 10, "consumption": 2},
              "Ferraria":{"fuel": 50, "strength": 300, "consumption": 25}}
