TICKET_PRICE = 10 

tickets_ramaining = 100 

#keep running logical until there are no tickets remaining.
while tickets_ramaining >= 1:
# output how many tickets remaining using the tickets_remaining variable
        print("Number of remaining tickets: {}".format(tickets_ramaining))

    # Gather the user's name and assign it to a new variable

        user_name = input("What is your name: ")

    # prompt the user by name and ask how many tickets they would like
        number_of_tickets_wanted = int(input("Hello, {}! How many tickets would you like? (Price per ticket: ${}.00) ".format(user_name, TICKET_PRICE)))
    #Calc the price (number_of_ticket_wanted * the price) and assign to a variable
        total = (TICKET_PRICE * number_of_tickets_wanted)
    #outputthe price to the screen

        print("Total: ${}.00 for {} tickets ".format(total, number_of_tickets_wanted))

    # prompt user if they want to proceed. Y/N?
        confirmation = input("Are you sure you want to proceed with purchase of {} tickets for a total of ${}.00 USD? Y/N ".format(number_of_tickets_wanted, total ))
    #If they want to proceed:
        if confirmation.upper() == "Y":
        #print out "SOLD!" to confirm purchase
        # gather cc information and process it
            print("SOLD!")
        # and then, decrement the tickets remaining by the number of tickets purchased
            tickets_ramaining -=  number_of_tickets_wanted

    #else...
        else:
            print("Thanks for wasting my time, {}".format(user_name))
        #thank them by name

print("The show is sold out. Sorry")    # notify user that the tickets are sold out. ]