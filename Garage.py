import os

parkingspaces = {
    "A1" : [" Vacant ", 0.00],
    "A2" : [" Vacant ", 0.00],
    "A3" : [" Vacant ", 0.00],
    "A4" : [" Vacant ", 0.00],
    "A5" : [" Vacant ", 0.00],
    "A6" : [" Vacant ", 0.00],
    "A7" : [" Vacant ", 0.00],
    "A8" : [" Vacant ", 0.00],
    "A9" : [" Vacant ", 0.00],
    "A0" : [" Vacant ", 0.00],
    "B1" : [" Vacant ", 0.00],
    "B2" : [" Vacant ", 0.00]
}


def displayParking():
    print("Current Parking Lot Status:")
    print("")
    for space in parkingspaces:
        print("| " + space + " | " + parkingspaces[space][0]+ " | ")
    print("")

class GarageParkingSpot:
    occupiedstatus = ["Occupied", 30.00]
    def __init__(self, space):
        self.space = [space, parkingspaces[space]]
        
    def takeTicket(self):
        parkingspaces[self.space[0]] = self.occupiedstatus
        self.space[1] = self.occupiedstatus

    def payForParking(self):
        if parkingspaces[self.space[0]][1] == 0.00:
            os.system('cls') #CLEAR SCREEN
            print("There is no fee for this space at this time.")
            print("It is currently vacant.")
            print(" ")
        else:
            fee = parkingspaces[self.space[0]][1]
            print(f"Your current fee is ${fee}. Please pay the fee to complete your ticket order.")
            justconfirmation = input("Press Enter to pay.")
            parkingspaces[self.space[0]] = [" Vacant ", 0.00]
            os.system('cls') #CLEAR SCREEN
            print("Thank you for your payment.")
            print("Thank you for using our Parking Lot. You may take 15 minutes to vacate the space.")
            print(" ")

OnOff = True
clearswitchscreen = None
while OnOff:
    if clearswitchscreen == None:
        os.system('cls') #CLEAR SCREEN
        clearswitchscreen = True
    
    displayParking()
    choicespace = input("Please select space (please choose letter and number): ")
    choicespace = choicespace[0].upper() + choicespace[1]
    currentTicket = GarageParkingSpot(choicespace)
    
    print(f"Current Chosen Ticket: {currentTicket.space}")
    print(" ")
    print("Please choose from the following for your chosen space:")
    print(" ")
    print("1. Reserve Space/Receive Ticket.")
    print("2. Pay Space Rental/Vacate Space.")
    print("3. Quit.")
    choice = int(input("Choice: "))

    if choice == 1:
        if currentTicket.space[1][0] == "Occupied":
            print("This space is already occupied.")
        else:
            currentTicket.takeTicket()
            os.system('cls') #CLEAR SCREEN
            print(f'Thank you for taking ticket ' + currentTicket.space[0] + '.')
            print(f'Your fee of ${currentTicket.space[1][1]} can be paid upon redemption of your Parking Ticket.')
    elif choice == 2:
        currentTicket.payForParking()
    elif choice == 3:
        print("Good day.")
        OnOff = False
        


























