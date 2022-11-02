# **Drone**
Drones Dispatch Controller
## Pre requirements
Python 3.8.5 --> as a language
virtualenv --> to create virtual environments. Install in CMD with the command `pip install virtualenv`


## Facility
###### For the installation of the dependencies, a virtual environment must initially be created for the project.
1. In the root folder of the project, using the IDE terminal type: `virtualenv 'virtual_environment_name'`
2. Activate the virtual environment. Move to the Script folder of the virtual environment:

    `cd 'virtual_environment' `

    `cdScript`

    `activate`

    _**NOTE:** The virtual environment has been activated correctly when we see in the terminal in front of the project path
in parentheses the name of the virtual environment:_ `('virtual_environment_name') 'project_path'`

4. Install the dependencies found in the requirements.txt file. To install them in list format use
the command `pip install -r requirements.txt`

## Setting
1. Configure the connection to the Database:
    
    Django uses SQLite3 as the default database. To have our local database in sqlite3 in the
    `settings.py` file should contain the following settings:
    
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
        
    Note: user, password (admin, Admin1234) for admin of django

2.  Check that there are no errors in our configuration:

    Type in the IDE terminal `python manage.py check`
    
    The successful response should be: `System check identified no issues (0 silenced).`
    
#### _DONE !!!_


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
