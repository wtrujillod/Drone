# **Drone**
Drones Dispatch Controller



## Assumptions

### Assuming the mAh capacity of each drone according to its model, we have to:

Lightweight with 900mAh 

Middleweight with 1200mAh 

Cruiserweight with 3000mAh 

Heavyweight with 6200mAh 

### Assuming the following formulas to calculate the battery level of the drone:
**Concepts:**

Battery capacity percentage (%BC)
###### defined when registering a drone

mAh capacity (C) 
###### assumed according to the drone model, defined in the previous description

Drone battery level (%BL)
###### assumed to be 100 percent when registering the drone

Minimum battery percentage (%MB)
###### defined according to the minimum battery needed for the drone model, assuming that Light Weight is 2%, Medium Weight is 5%, Cruiser Weight is 8%, Heavy Weight is 10% 

Real battery capacity (RBC)

Available battery capacity (ABC)

Load weight percentage (%LW)

Battery consumption by weight percentage of the load (BCLW)

Percentage of battery consumption by load weight (%BCLW)

**Formulas:**

%LW = (weight / weight limit) * 100

RBC = (%BC / 100) * C

ABC = ((%BL - %MB) / 100) * RBC

BCLW = (%LW / 100) * ABC

%BCLW = (BCLW / RBC) * 100

%BL = %BL - %BCLW
