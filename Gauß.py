import random

#Drei Türen Problem

doors = []
doors_left = []

for i in range(1000):
    doors.append(i+1)

door_with_car = random.choice(doors)
print(door_with_car)
doors_left.append(doors.remove(door_with_car))
first_choice = random.choice(doors)
if door_with_car == first_choice:
    print("True")
else:
    print("False")
    for i in range(998):
        a = random.choice(doors_left)
        doors.remove(a)
        doors_left.remove(a)
    print(doors)
    