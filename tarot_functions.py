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
spread = input("What tarot spread would you like today?")

if spread.upper() == "BASIC SPREAD":
    print(str(basic_spread()))
elif spread.upper() == "CROSS SPREAD":
    print(str(cross_spread()))
elif spread.upper() == "SINGLE SPREAD":
    print(str(single_spread()))
else:
    print("Not a valid input")

