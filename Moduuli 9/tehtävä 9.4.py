import random
class Auto:
    def __init__(self, registry, topspeed=0, currentspeed=0, distance_traveled=0):
        self.registry = registry
        self.topspeed = topspeed
        self.currentspeed = currentspeed
        self.distance_traveled = distance_traveled

    def hours(self, hours):
        self.distance_traveled += hours * self.currentspeed

    def accelerate(self, speed):
        self.currentspeed += speed
        if self.currentspeed < 0:
            self.currentspeed = 0
        elif self.currentspeed > self.topspeed:
            self.currentspeed = self.topspeed

    def __repr__(self):
        return (f"{self.registry}: Final speed = {self.currentspeed} km/h, "
                f"Distance travelled = {self.distance_traveled} km, Top Speed = {self.topspeed} km/h")

cars = []
for i in range(11):
    auto = Auto(f"ABC-{i}", random.randint(100,200))
    cars.append(auto)

goal_reached = False

while goal_reached == False:
    for auto in cars:
        auto.accelerate(random.randint(-10, 15))
        auto.hours(1)
        if auto.distance_traveled >= 10000:
            goal_reached = True
            break

for car in cars:
    print(car)