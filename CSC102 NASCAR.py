
##################################################################################################################
#                                                                                                                #
# Define a class called Car with the following attributes:                                                       #
#   1. Total Odometer Miles                                                                                      #
#   2. Speed in miles per hour                                                                                   #
#   3. Driver Name                                                                                               #
#   4. Sponsor                                                                                                   #
# The total odometer miles and speed should be initialized to zero.                                              #
#                                                                                                                #
# Create a list of 20 unique vehicles with random (or real) driver and sponsor names.                            #
#                                                                                                                #
# Your main program should simulate the progress of the vehicles in the race.                                    #
#   Every simulated minute, the vehicles pick a new random speed between 1 and 120,                              #
#   and their odometer miles are updated every minute using this equation:                                       #
#       odometer_miles = odometer_miles + speed * time                                                           #
#   Since speed is in miles per hour, time should be in hours as well (1 minute is 1/60th of an hour).           #
#                                                                                                                #
# The first car to reach 500 miles should be declared the winner by printing the driver name and sponsor name.   #
#                                                                                                                #
################################################################################################################ #
#                                                                                                                #
# * Include any useful methods in your class definition that you see fit.                                        #
# * Be sure to use comments for both structure of the program and documentation of the code.                     #
# * All code must completely be your own individual work product.                                                #
# * Post your valid code (Valid means python version 3.1 or 3.2) *.py file here.                                 #
#                                                                                                                #
##################################################################################################################

from random import randint                                                                          # import the randint function
from time import sleep                                                                              # import the sleep function

class Car():                                                                                        # This creates a class blueprint
    
    def __init__(self):                                                                             # These are the attributes in class
        self.__odometer = 0
        self.__speed = 0
        self.__driver = ''
        self.__sponsor = ''
        
    def setOdometer(self):                                                  # Function to update object odometer. Speed * simulated time. 1m is 1s. So you are traveling 1m per update (each second).
        time = .017                                                                                 # To increase speed of the program change this variable to 1, it will finish 100 times faster.
        self.__odometer = self.__odometer + self.__speed*time 
        return
    
    def setSpeed(self):                                                                             # Function to update object speed
        self.__speed = randint(1, 120)
        return
    
    def setDrivers(self, i):                                                                        # This function will set drivers name to each object
        # The list below will be used later to assign names to each car in a list.
        names = ['Kurt', 'Kevin', 'Chris', 'Danica', 'Clint',
                'Charles', 'Matt', 'Ty', 'Gray', 'Erik',
                'David', 'Daniel', 'Jim', 'Jack', 'John',
                'Paul', 'Adam', 'Kenneth', 'Justin', 'Bobby']
        driverName = names[i]
        self.__driver = driverName
        return self.__driver 
    
    def setSponsor(self, i):                                                                        # This function will set sponsor name to each object
        # The list below will be used later to assign sponsors to each car in a list.
        sponsor = ['Menards', 'Smuckers', 'Aarons', 'Target', 'Banquet',
                  'Subway', 'Pepsi', 'Big Lots', 'Budweiser', 'Carquest',
                  'Taco Bell', 'Cheerios', 'DeWalt', 'Monster', 'Fastenal',
                  'FedEx', 'GEICO', 'Lowes', 'M&Ms', 'McDonalds']
        sponsorName = sponsor[i]
        self.__sponsor = sponsorName
        return self.__sponsor

    def getOdometer(self):                                                                          # function to send odometer updates back to object
        return float(self.__odometer)
    def getSpeed(self):                                                                             # function to send speed updates back to object
        return float(self.__speed)
    def getDrivers(self):                                                                           # function to send the drivers name back to object
        return self.__driver 
    def getSponsor(self):                                                                           # function to send the sponsors name back to object
        return self.__sponsor
    
def victoryCondition(carsList):                                                                     # Function to Create a victory condition
    for i in carsList:                                                                              # Look at every car
        miles = i.getOdometer()                                                                     # create temporary variable to store the objects odometer
        if miles >= 500:                                                                            # if i in carsList has their odometer attribute equal to or greater than 500
            print(i.getDrivers(),'sponsored by',i.getSponsor(),'is the winner!')                    # print the cars name and sponsor that got to 500 miles first.
            return True
    return False

def updateOdometers(carsList):                                                                      # Function to update odometer for every object in carsList
    for i in carsList:
        i.setOdometer()
        displayList(i)
        
def updateAllSpeed(carsList):                                                                       # Function to update speeds of every object in carsList
    for i in carsList:
        i.setSpeed()

def displayList(car):                                                                               # Function to display speeds of the called object
        print('Name: ',car.getDrivers(),'\t','Sponsor: ', car.getSponsor(),'\t', 'Speed: ',car.getSpeed(),'\t','Odometer: ','{:,.2f}'.format(car.getOdometer()))

def makeList():                                                                                     # Function to create and store objects of the Car blueprint in a list.
    carsList = []
    for i in range(20):                                                                             # Change range(20) to change the number of racers.
        car = Car()
        carsList.append(car)
        car.setDrivers(i)
        car.setSponsor(i)
    return carsList
    
def main():                                                                                         # Main function
    carsList = makeList()                                                                           # carsList is a list of objects assigned in the makeList function
    while victoryCondition(carsList) is False:                                                      # while victoryCondition returns false
        updateAllSpeed(carsList)                                                                    # Update the speed of all cars
        updateOdometers(carsList)                                                                   # update the odometer of all cars
        print('')                                                                                   # print blank line for formatting
        sleep(1)                                                                                    # delay 1s for timing and easier readability

main()                                                                                              # Calls the main function
