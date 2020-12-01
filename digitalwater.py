# digital-watermeter
#automatic digital water meter simple calculation code
import math
import time
import numpy as np
import statistics

dia = 20
mem=int(input("enter the number of members"))
extracost=[]
watersupply=[]
day=1

def final():
    totalwater = sum(watersupply)
    totalfine = sum(extracost)
    print("the total quantity of water supplied for", day, "days were", totalwater)
    print("the total fine for extra water supplied for", day, "days were", totalfine)
    empty = np.array([])
    empty1 = np.array([])
    watersupplied = np.array(watersupply)
    fine_perday = np.array(extracost)
    combined = np.append(empty, watersupplied)
    combined1 = np.append(empty1, extracost)
    family_report = np.array((combined, combined1))
    print(family_report)

def stat():
    average=statistics.mean(watersupply)
    print("the average water supplied for the house is",average)
    maximum=max(watersupply)
    print("the highest water supplied per day for the house is", maximum)


while(day<=31):
    print("record for day",day)
    def velocity():
        radius=dia/2
        rotation=int(input('enter the values of rotation per minute(values from motion sensor)'))
        vel=2*(math.pi)*60*radius*rotation/1000
        print("the velocity of the water is",vel,"m/s")
        return(vel)

    def area():
        diainm=dia/1000
        area=((math.pi)*(diainm)**2)/4
        print("the area of the pipe is", area ,"m2")
        return(area)

    Q=(velocity()*area())*1000
    print("the discharge through the pipe is",Q,"litres/s")

    runtime=int(input("enter the time in seconds"))
    waterused=float(Q*runtime)
    print("the total amount of water used today is",waterused,"litres")
    watersupply.append(waterused)

    demand=mem*120+mem*50
    if(waterused<demand):
        print("no extra cost")
        extracost.append(0)
    elif((waterused>demand) and (waterused<(2*demand))):
        print("there is a fine")
        fine=(waterused/5)
        print(fine)
        extracost.append(fine)
    else:
        fine = (waterused /5)
        print(fine)
        extracost.append(fine)
        print("pipe lock at day",day)
        break
    day=day+1
    print("the daywise watersupply are",watersupply,"litres")
    print("the daywise extracost are",extracost,"rupees")



f=open("waterfile.txt","w")
final()
stat()
f.close()

f=open("waterfile.txt","r")
print(f.read())



