import random
import time

# create classes at top or in a seperate file
class Car:
    def __init__(self, name="unknown", speed=0, location=0):
        self.name = name
        self.speed = speed
        self.location = location
        
    def move(self):
        self.speed = random.randint(3, 6)    #3-6
        self.location += self.speed


# write code below the classes and methods
car1 = Car()
car1.name = "lambo"
car1.location = 0
car1.speed = 0
car2 = Car("GT3", 0, 0)
car3 = Car("ferrari", 0, 0)

#race the cars to 100
while car1.location < 100 and car2.location < 100 and car3.location < 100:
    car1.move()
    car2.move()
    car3.move()
    
    print(f"{car1.name}: {car1.location}:")
    time.sleep(1)
    print(car2.name +":",car2.location)
    print(car3.name +":",car3.location)

print()    
if car1.location > car2.location and car1.location > car3.location:
        print(car1.name + " won the race!")
elif car2.location > car1.location and car2.location > car3.location:
        print(car2.name + "won the race!")
elif car3.location > car1.location and car3.location > car2.location:
            print(car2.name + "won the race!")
else:
        print("The race is a tie!")