#!/bin/python3

# Drip edge waste calculator

# Takes input for actual eaves and rakes
actual_e = float(input("What is the actual measurement for the eaves? "))
actual_r = float(input("What is the actual measurement for the rakes? "))

# Adds waste
waste_e = actual_e * 1.06
waste_r = actual_r * 1.06

# Outputs drip edge lengths for Eaves w/ waste
print("You will need {} lf of drip edge for the Eaves.".format(waste_e))

# Outputs drip edge lengths for Rakes w/ waste
print("You will need {} lf of drip edge for the Rakes.".format(waste_r))

# Outputs actual length
print("Actual length of Eaves and Rakes is {}.".format(actual_e + actual_r))
# Outputs total length
print("You will need {} lf of drip edge total for this job.".format(waste_e + waste_r))
