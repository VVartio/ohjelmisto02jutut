class Auto:

    def __init__(self, registry, topspeed=0, currentspeed=0, distance_traveled=0, accelerate=0):
        self.registry = registry
        self.topspeed = topspeed
        self.currentspeed = currentspeed
        self.distance_traveled = distance_traveled
        self.accelerate = accelerate

auto = Auto("ABC-123", 142)

auto.currentspeed += auto.accelerate

while auto.currentspeed < auto.topspeed:
    auto.currentspeed += 30
    auto.currentspeed += 70
    auto.currentspeed += 50
    if auto.currentspeed >= auto.topspeed:
        auto.currentspeed = auto.topspeed

auto.currentspeed -= 200

if auto.currentspeed < 0:
    auto.currentspeed = 0

print(f"The car has been registered as: {auto.registry}, with a top speed of {auto.topspeed} km/h.")
print(f"Current speed: {auto.currentspeed}, distance traveled: {auto.distance_traveled}.")