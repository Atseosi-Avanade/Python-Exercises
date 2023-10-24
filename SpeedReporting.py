"""
Write a program to find distance given speed and time
"""
import sys
speed = None
distance = None
time = None

speed = input("Input speed: ")
distance = input("Input distance: ")
time = input("Input time: ")

if speed != "" and time != "":
    print(f"Distance is {int(speed) * int(time)}")
elif speed != "" and distance != "":
    print(f"Time is {int(distance) / int(speed)}")
elif time != "" and distance != "":
    print(f"Speed is {int(distance) / int(time)}")
else:
    print("I need more info!")


sys.exit(0)
