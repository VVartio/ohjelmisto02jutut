class Auto:

    def __init__(self, registry, topspeed=0, currentspeed=0,
                 distance_traveled=0, accelerate=0):
        self.registry = registry
        self.topspeed = topspeed
        self.currentspeed = currentspeed
        self.distance_traveled = distance_traveled
        self.accelerate = accelerate
    def hours(self, hours):
        auto.distance_traveled += hours * auto.currentspeed


auto = Auto("ABC-123", 142, distance_traveled = 2000)

"""
while auto.currentspeed < auto.topspeed and auto.accelerate != "no":
    #auto.accelerate = input("acceleration?")
    auto.currentspeed += auto.accelerate
    if auto.currentspeed >= auto.topspeed:
        auto.currentspeed = auto.topspeed
        print(auto.currentspeed)
    else:
        print(auto.currentspeed)
"""
#sudden break
auto.currentspeed += 60

if auto.currentspeed < 0:
    auto.currentspeed = 0

auto.hours(1.5)
print(auto.hours)

print(f"The car has been registered as: {auto.registry}, with a top speed of {auto.topspeed} km/h.")
print(f"Current speed: {auto.currentspeed}, distance traveled: {auto.distance_traveled}.")