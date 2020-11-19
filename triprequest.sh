#!/bin/bash

# Trip Charge Calculator

# This script takes miles, travel hours and time at project
# and calculates all the amounts to put on pay request.

# Asks for name of Customer
read -p "Enter the name of the customer: " CUST_NAME

# Asks for how many miles to job
read -p "How many miles away was the job? " TRAV_MILES

# Asks for how many minutes travel time
read -p "How many minutes of travel time? " TRAV_MINS

# Asks how many hours at job
read -p "How many hours did you work at the jobsite? " XTRA_TIME
# if [[ "${XTRA_TIME}" -eq 0 ]]
# then
#     echo "Surely you must have done something!?"
#     exit 1
# else
#     exit 0
# fi

# Calculates minutes into hours and multiplies by $35 per hour.
# TRAV_HOURS=$(( "${TRAV_MINS}" * 2 / 60 * 35 ))
TRAVCALC=$(( "${TRAV_MINS}" * 2 ))
# TRAV_HOURS=$(( "${TRAVCALC}" / 60 * 35 ))
TRAVCALC2=$(( "${TRAVCALC}" / 60 ))
TRAV_HOURS=$(( "${TRAVCALC2}" * 35 ))
# Calculates travel miles plus travel hours
TRAV=$(( "${TRAV_MILES}" + "${TRAV_HOURS}" ))
# Calculates extra time and multiplies by $35 per hour.
XTRA=$(( "${XTRA_TIME}" * 35 ))
# Calculates total
TRIP=$(( "${TRAV}" + "${XTRA}" ))

# Outputs $0 in totals if exit error occurs
if [[ exit -eq 0 ]]
then
    TRAV=0
    XTRA=0
    TRIP=0
fi

# Outputs everything in a neat format for quick pay requests
echo " *************************************************** "
echo "Trip Charge Pay Request for ${CUST_NAME}:"
echo "You travelled ${TRAV_MILES} miles and it took ${TRAV_MINS} minutes."
echo "You also worked another ${XTRA_TIME} hours on the job."
echo "Travel Minutes: ${TRAV_MINS} > Travel Hours: ${TRAV_HOURS}."
echo "Trav Calc: ${TRAVCALC} (Travel minutes * 2)."
echo "Trav Calc2: ${TRAVCALC2} (Travcalc / 60)."
echo " *************************************************** "
echo "You earned $ ${TRAV}.00 for travelling."
echo "You earned $ ${XTRA}.00 at the location."
echo "You earned $ ${TRIP}.00 total for ${CUST_NAME}."



