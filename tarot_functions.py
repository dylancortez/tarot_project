from tarot_data import CardsList
import random

#defining function to return basic 3 card spread for Past, Present, and Future
def basic_spread():
    past_reading = random.choice(CardsList)
    present_reading = random.choice(CardsList)
    future_reading = random.choice(CardsList)
    reading = "Past: ", past_reading, "Present: ", present_reading, "Future: ", future_reading
    return str(reading)

#defining function to return a single-card spread
def single_spread():
    reading = random.choice(CardsList)
    return str(reading)

#print readout of basic 3 card spread
print(str(basic_spread()))