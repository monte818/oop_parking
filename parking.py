import time

class Parking:
   
    def __init__(self, tickets, currentTicket):
        self.tickets = [i for i in range(1, tickets + 1)]  
        self.spots = [f"{chr(65 + i)}{j}" for i in range(26) for j in range(1, 6)]  
        # self.tickets = tickets these were old methods
        # self.spot = spots
        self.currentTicket = currentTicket

    def takeTicket(self):
        if len(self.tickets) > 0:
            print("Enter your license plate number for a ticket! if you don't want to park here then say exit")
            plate = input("what is your license plate number? ")
            if plate in self.currentTicket:
                print("You already have a ticket. you can not get another")
            elif plate.lower() == "exit":
                print("thank you hope to see you soon!")
            else:
                ticket = self.tickets.pop(0)
                spot = self.spots.pop(0)
                self.currentTicket[plate] = {"ticket": ticket, "spot": spot, "paid": False, "entry_time": time.time()}
                print(f'your ticket number is {ticket} and your spot is {spot}')
        else:
            print("sorry lot is full come again next time :)")
     
    def payParking(self):
        if not self.currentTicket:
            print("No valid tickets found. Please take a ticket first")
            return

        platePay = input("what is your license plate number? ")
        while platePay not in self.currentTicket:
            print("incorrect license plate try again or check spelling")
            platePay = input("what is your license plate number? ")
        
        parking_info = self.currentTicket[platePay]
        entry_time = parking_info["entry_time"]
        exit_time = time.time()
        parking_duration = exit_time - entry_time
        cost = self.calculate_cost(parking_duration)

        if not parking_info["paid"]:
            print(f"The cost for your parking is: ${cost:.2f}")
            pay_now = input("Would you like to pay now? (yes/no): ")
            if pay_now.lower() == "yes":
                user_input = float(input("Please enter the amount you would like to pay: "))
                if user_input >= cost:
                    self.currentTicket[platePay]["paid"] = True
                    remaining_time = self.calculate_remaining_time(parking_duration)
                    print(f"You have paid ${cost:.2f}. You have {remaining_time} remaining to leave.")
                else:
                    print(f"You must pay at least ${cost:.2f} to leave.")
            else:
                print("You must pay for your ticket before leaving.")
        else:
            print("Your ticket is already paid. You can leave without further payment.")

    def calculate_cost(self, parking_duration):
        if parking_duration <= 900:  # 15 minutes
            return 0.50
        elif parking_duration <= 1800:  # 30 minutes
            return 1.00
        elif parking_duration <= 3600:  # 1 hour
            return 2.00
        else:
            additional_time = parking_duration - 3600
            additional_cost = (additional_time // 900) * 1.00
            return 2.00 + additional_cost
    
    def calculate_remaining_time(self, parking_duration):
        # remaining_seconds = max(0, 3600 - parking_duration)
        # remaining_minutes = remaining_seconds // 60
        # return f"{remaining_minutes} minutes"
        if parking_duration <= 900:  # 15 minutes
            remaining_seconds = max(0, 900 - parking_duration)
        elif parking_duration <= 1800:  # 30 minutes
            remaining_seconds = max(0, 1800 - parking_duration)
        elif parking_duration <= 3600:  # 1 hour
            remaining_seconds = max(0, 3600 - parking_duration)
        else:
            remaining_seconds = 0

        remaining_minutes = remaining_seconds // 60
        return f"{remaining_minutes} minutes"

    def leaveGarage(self):
        if not self.currentTicket:
            print("No valid tickets found. Please take a ticket first.")
            return

        plateLeave = input("What is your license plate number? ")
        if plateLeave in self.currentTicket:
            parking_info = self.currentTicket[plateLeave]
            entry_time = parking_info["entry_time"]
            exit_time = time.time()
            parking_duration = exit_time - entry_time
            cost = self.calculate_cost(parking_duration)

            if parking_info["paid"]:
                ticket = parking_info["ticket"]
                spot = parking_info["spot"]
                self.tickets.append(ticket)
                self.spots.append(spot)
                print(f"Thank you for using our parking services. Come back soon!")
                print(f"Your parking duration: {int(parking_duration / 60)} minutes")
            else:
                print(f"Your parking duration: {int(parking_duration / 60)} minutes")
                print(f"The cost for your parking is: ${cost:.2f}")
                pay_now = input("Would you like to pay now? (yes/no): ")
                if pay_now.lower() == "yes":
                    user_input = float(input("Please enter the amount you would like to pay: "))
                    if user_input >= cost:
                        parking_info["paid"] = True
                        print(f"You have paid ${cost:.2f}. You can now leave.")
                        ticket = parking_info["ticket"]
                        spot = parking_info["spot"]
                        self.tickets.append(ticket)
                        self.spots.append(spot)
                    else:
                        print(f"You must pay at least ${cost:.2f} to leave.")
                else:
                    print("You must pay for your ticket before leaving.")
        else:
            print("License plate not found in the current tickets list.")


theater_lot = Parking(20, {})

def run():
    while True:
        menu = input("Welcome to the parking lot: Take ticket [t], pay for ticket [p], or leave parking garage [l]: ")
        if menu.lower() == "t":
            theater_lot.takeTicket()
            print(theater_lot.currentTicket)
        elif menu.lower() == "p":
            theater_lot.payParking()
        elif menu.lower() == "l":
            theater_lot.leaveGarage()
        else:
            break

if __name__ == "__main__":
    run()

 # Ran various test to see if the tickets would be sent back to the list and same with the spots.
 

     
# print(theater_lot.tickets)
# print(theater_lot.spots)
# theater_lot.takeTicket()
# theater_lot.payParking()
# run()