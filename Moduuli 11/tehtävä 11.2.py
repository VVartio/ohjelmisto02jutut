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
                f"Automittarilukema = {self.distance_traveled} km, Top Speed = {self.topspeed} km/h")

class Sähköauto(Auto):
    def __init__(self, registry, top_speed, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(registry, top_speed)

class Pollttomoottoriauto(Auto):
    def __init__(self, registry, top_speed, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(registry, top_speed)

cars = []

cars.append(Sähköauto("ABC-15", 180, 52.5))
cars.append(Pollttomoottoriauto("ADC-123", 165, 32.3))

goal_reached = False
hour_count = 0
while goal_reached == False:
    for auto in cars:
        auto.accelerate(random.randint(-10, 15))
        auto.hours(1)
        hour_count += 1
        if hour_count >= 3:
            goal_reached = True
            break

for car in cars:
    print(car)