TICKET_PRICE = 10 
SERVICE_CHARGE = 2

tickets_ramaining = 100 

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_ramaining >= 1:
        print("Number of remaining tickets: {}".format(tickets_ramaining))
        user_name = input("What is your name: ")
        number_of_tickets = input("Hello, {}! How many tickets would you like? (Price per ticket: ${}.00) ".format(user_name, TICKET_PRICE))
        try:
            number_of_tickets = int(number_of_tickets)
            if number_of_tickets > tickets_ramaining:
                raise ValueError("There are only {} tickets remaining".format(tickets_ramaining))
        except ValueError as err:

            print("Oh no! That is not a valid value. {}. Try again.".format(err))
        else:
            total = calculate_price(number_of_tickets)
            print("Total: ${}.00 for {} tickets ".format(total, number_of_tickets))
            confirmation = input("Are you sure you want to proceed with purchase of {} tickets for a total of ${}.00 USD? Y/N ".format(number_of_tickets, total ))
            if confirmation.upper() == "Y":
                #3 TODO gather cc info and process
                print("SOLD!")
                tickets_ramaining -=  number_of_tickets
            else:
                print("Thanks for wasting my time, {}".format(user_name))

print("The show is sold out. Sorry")