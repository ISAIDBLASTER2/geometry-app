import math
import tkinter as tk
import geometry as geo
while True:    
    a = input("shape?: ")

    if a == "circle":
        r = input("radius: ")
        ans = geo.areacircle(r)
        print(f"{ans:.2f}")
    elif a == "square":
        x = input("length of a side: ")
        ans = geo.areasqr(x)
        print(f"{ans:.2f}")
    elif a == "rectangle":
        x = input("first side: ")
        y = input("second side: ")
        ans = geo.arearect(x , y)
        print(f"{ans:.2f}")
    else:
        print("shape not supported or invalid shape")
    a = input("exit: ")
    if a == "yes":
        print("disconnecting from servers.. dns3203 disconnected")
        break
    else:
        continue 