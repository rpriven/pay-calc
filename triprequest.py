#!/bin/python3

# Trip Charge Calculator
# Python Reboot 9/18/20

# This script takes miles, travel hours and time at project
# and calculates all the amounts to put on pay request.

class color:
    PURPLE = '033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    SHADED = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
# Asks for name of Customer.
cust_name = input("Enter the name of the customer: ")   
      
# Asks for how many miles to job.
miles_away = float(input("How many miles away was the job? "))

# Asks for how many minutes of travel time.
trav_mins = float(input("How many minutes of travel time? "))

# Asks how many hours worked at job.
xtra_time = float(input("How many hours did you work at the jobsite? "))

if ( xtra_time == " " or 0) : print("Surely you must have done something!?")

# Calculates minutes into hours and multiplies by $35 per hour.
# Multiplies travel minutes * 2.
travcalc = trav_mins * 2
# If travel minutes (*2) are greater than or equal to 60, divide by 
# 60 to get travel hours times $35 per hour.
if ( travcalc >= 60 ) : trav_hours = travcalc/60 * 35
# If travel minutes are less than 60, multiply by $.58333 per minute.
if ( travcalc < 60 ) : trav_hours = travcalc * .58333
trav_miles = miles_away * 2 / 2

# Calculates travel miles plus travel hours.
trav = trav_miles + trav_hours
# Calculates extra time and multiplies by $35 per hour.
xtra = xtra_time * 35
# Calculates total.
trip = trav + xtra

# Outputs $0 in totals if exit error occurs.
if ( exit == 1 ) : trav = xtra = trip = 0

# Outputs everything in a neat format for quick pay requests.
print('\n')
print(" *************************************************** ")
print(color.UNDERLINE + "Trip Charge Pay Request for " + cust_name + ":" + color.END)
print(" You travelled " + str(trav_miles * 2) + " miles and it took " + str(travcalc) + " minutes.")
print(" " + color.UNDERLINE + "You also worked another " + str(xtra_time) + " hours on the job." + color.END)
print("   " + color.UNDERLINE + "Distance:" + color.END + " " + str(miles_away) + " miles    " + color.UNDERLINE + "Time:" + color.END + " " + str(trav_mins) + " minutes")
print("   " + color.UNDERLINE + "Total Miles:" + color.END + " " + str(trav_miles * 2) + " * .50 per Mile = $ " + str(miles_away))
print("   " + color.UNDERLINE + "Total Minutes:" + color.END + " " + str(travcalc) + " / 60 = " + color.BOLD + str(round(travcalc/60,2)) + color.END + " Travel Hours")
print(" *************************************************** ")
print("   You earned " + color.BOLD + "$ " + str(round(miles_away,2)) + color.END + " for your truck.")
print("   You earned " + color.BOLD + "$ " + str(round(trav_hours,2)) + color.END + " for travelling.")
print("   You earned " + color.BOLD + "$ " + str(round(xtra,2)) + color.END + " while at the location.")
print(" =================================================== ")
print(color.BOLD + "   You earned $ " + str(round(trip,2)) + " total for Customer: " + cust_name + "." + color.END)


