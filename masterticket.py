TICKET_PRICE = 10 

tickets_ramaining = 100 

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