class Auto:
    currentspeed = 0
    topspeed = 0
    distance_traveled = 0
    def __init__(self, registry, topspeed):
        self.registry = registry
        self.topspeed = topspeed

auto = Auto(input("reg"), input("speed"))

print(f"The car has been registered as: {auto.registry}, with a top speed of {auto.topspeed} km/h.")
print(f"Current speed: {auto.currentspeed}, distance traveled: {auto.distance_traveled}.")