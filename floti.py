import time
import random

class Fleet:
    wind = [-7, 5, -3, 0, 7, -5, 7]
    under_water = [10, 0, 10]
    enemy = [1, 10, 30, 50, 0, 101]

    def __init__(self, name, speed, weight, luggage, ammo, distance):
        self.name = name
        self.speed = speed
        self.weight = weight
        self.luggage = luggage
        self.ammo = ammo
        self.distance = distance

    def general_speed(self):
        velocity = (self.weight / self.speed + random.choice(Fleet.wind)) * 15 - (self.luggage / 100)
        print(f'gemis "{self.name}" sichqarea {velocity}')
        counting = 0
        while True:
            if self.distance <= 0:
                print("gemma '{}'  danishnulebis adgils miaghwia {} satshi".format(self.name, counting))
                break
            self.distance -= velocity
            counting += 1
            time.sleep(0.03)
        print("- - - - - - - - - -")

    def submarine_speed(self):
        velocity = (self.weight / self.speed + random.choice(Fleet.under_water)) * 30 - (self.luggage / 100)
        print(f'gemis "{self.name}" sichqarea {velocity}')
        counting = 0
        while True:
            if self.distance <= 0:
                print("gemma '{}'  danishnulebis adgils miaghwia {} satshi".format(self.name, counting))
                break
            self.distance -= velocity
            counting += 1
            time.sleep(0.1)
        print("- - - - - - - - - -")

    def rifle(self):
        if self.ammo >= random.randrange(2, 101):
            print("mteri ganadgurebulia {} - s mier".format(self.name))
        else:
            print("samwuxarod gemi '{}' ganadgurebulia :( ".format(self.name))
