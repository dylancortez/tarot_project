from tarot_data import MajArcana, MinArcana, MinReversed
import random

#defining function to return basic 3 card spread for Past, Present, and Future
def basic_spread():
    choice1 = random.choice(MajArcana)
    choice2 = random.choice(MajArcana)
    choice3 = random.choice(MinArcana)
    choice4 = random.choice(MinArcana)
    choice5 = random.choice(MinReversed)
    choice6 = random.choice(MinReversed)
    choice_list = [choice1, choice2, choice3, choice4, choice5, choice6]
    past_reading = random.choice(choice_list)
    present_reading = random.choice(choice_list)
    future_reading = random.choice(choice_list)
    reading = "Past:", past_reading, "Present:", present_reading, "Future:", future_reading
    return str(reading)

#defining function to return a single-card spread
def single_spread():
    reading = random.choice(MajArcana)
    return str(reading)

#defining a 5 card spread, building upon the 3 card basic_spread()
def cross_spread():
    core_reading = random.choice(MajArcana)
    potential_reading = random.choice(MajArcana)
    new_reading = "Core: ", core_reading, "Potential: ", potential_reading
    return basic_spread(), new_reading

#print readout of basic 3 card spread
print(str(basic_spread()))
