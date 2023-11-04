class Parking:
   
    def __init__(self, tickets, currentTicket):
        self.tickets = [i for i in range(1, tickets + 1)]  
        self.spots = [f"{chr(65 + i)}{j}" for i in range(26) for j in range(1, 6)]  
        # self.tickets = tickets these were old methods
        # self.spot = spots
        self.currentTicket = currentTicket

    def takeTicket(self):
        if len(self.tickets) > 0:
            print("Welcome to the parking lot grab your ticket from here! ")
            plate = input("what is your license plate number? ")
            ticket = self.tickets.pop(0)
            spot = self.spots.pop(0)
            self.currentTicket[plate] = {"ticket": ticket, "spot": spot, "paid": False}
            print(f'your ticket number is {ticket} and your spot is {spot}')
        else:
            print("sorry lot is full come again next time :)")
    
    def payParking(self):
        platePay = input("what is your license plate number? ")
        while platePay not in self.currentTicket:
            print("incorrect license plate try again or check spelling")
            platePay = input("what is your license plate number? ")
        user_input = float(input("Please enter amount you would like to pay for parking ticket "))
        if user_input <= .50:
            self.currentTicket[platePay]["paid"] = True
            print("you have 15 minutes! ")
        elif user_input <= 1.00:
            self.currentTicket[platePay]["paid"] = True
            print("you have 30 minutes! ")
        elif user_input <= 2.00:
            self.currentTicket[platePay]["paid"] = True
            print("You have 1 Hour! ")
        else:
            print("try another value")
    
    def leaveGarage(self):
        plateLeave = input("What is your license plate number? ")
        if plateLeave in self.currentTicket:
            parking_info = self.currentTicket.pop(plateLeave)
            ticket = parking_info["ticket"]
            spot = parking_info["spot"]
            self.tickets.append(ticket)
            self.spots.append(spot)
            print(f"Thank you for using our parking services. Come back soon!")
        else:
            print("License plate not found in the current tickets list.")

theater_lot = Parking(20, {})

def run():
    question = input("Welcome to the parking lot would you like to take a ticket? ")
    if question.lower() == "yes":
        theater_lot.takeTicket()
    question_2 = input("would you like to pay for parking ticket now or later? ")
    if question_2.lower() == "now":
        theater_lot.payParking()
        print(theater_lot.currentTicket)
    else:
        print("you can pay later upon leaving!")
    question_3 = input("hey are you leaving the parking lot? ")
    if question_3.lower() == "yes" or "yeah":
        theater_lot.leaveGarage()
    else:
        print("alright dont forget to make sure your ticket is paid, for when you decide to leave, thank you!")

 # Ran various test to see if the tickets would be sent back to the list and same with the spots.
 

run()        
# print(theater_lot.tickets)
# print(theater_lot.spots)
# theater_lot.takeTicket()
# theater_lot.payParking()
# run()
