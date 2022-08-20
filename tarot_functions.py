from tarot_data import MajArcana, MinArcana, MinReversed
import random

#defining function to return basic 3 card spread for Past, Present, and Future
def basic_spread():
    lists = MajArcana + MinArcana + MinReversed
    past_reading = random.choice(lists)
    present_reading = random.choice(lists)
    future_reading = random.choice(lists)
    reading = "Past: {past} \n\nPresent: {present} \n\nFuture: {future}".format(past=past_reading, present=present_reading, future=future_reading)
    return str(reading)

#defining function to return a single-card spread
def single_spread():
    lists = MajArcana + MinArcana + MinReversed
    reading = random.choice(lists)
    return str(reading)

#defining a 5 card spread, building upon the 3 card basic_spread()
def cross_spread():
    lists = MajArcana + MinArcana + MinReversed
    past_reading = random.choice(lists)
    present_reading = random.choice(lists)
    future_reading = random.choice(lists)
    core_reading = random.choice(lists)
    potential_reading = random.choice(lists)
    new_reading = "Past: {past}\n\nPresent: {present}\n\nFuture: {future}\n\nCore: {core}\n\nPotential: {potential}".format(past=past_reading, present=present_reading, future=future_reading, core=core_reading, potential=potential_reading)
    return new_reading

#user input for what tarot spread they would like
input("What question do you have for me today?")

spread = input("What tarot spread would you like today? Basic, Single, or Cross spread?")

if spread.upper() == "BASIC SPREAD" or spread.upper() == "BASIC":
    print(str(basic_spread()))
elif spread.upper() == "CROSS SPREAD" or spread.upper() == "CROSS":
    print(str(cross_spread()))
elif spread.upper() == "SINGLE SPREAD" or spread.upper() == "SINGLE":
    print(str(single_spread()))
else:
    ValueError("Please select an appropriate spread type!")

