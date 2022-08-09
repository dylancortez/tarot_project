import random
MajorArcana = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Justice", "The Hermit", "Wheel of Fortune", "Strength", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]
MajorArcanaValues = list(range(22))
TarotCards = {MajorArcana[i]: MajorArcanaValues[i] for i in range(len(MajorArcana))}

class TarotCard:
    def __init__(self, MajorArcana, MinorArcana="None"):
        self.MajorArcana = MajorArcana
        self.MinorArcana = MinorArcana
        self.ArcanaMeaning = ""
    def __repr__(self):
        return "{arcana} represents {meaning}.".format(arcana=self.MajorArcana, meaning=self.ArcanaMeaning)

# Tarot Reading Interpretations, info obtained from https://www.biddytarot.com/tarot-card-meanings/major-arcana/
CardsList = [TarotCard(_) for _ in MajorArcana]
CardsList[0].ArcanaMeaning = "new beginnings, opportunity, and potential. Throw caution to the wind and be ready to embrace the unknown, leaving behind any fear, worry or anxiety about what may or may not happen"
CardsList[1].ArcanaMeaning = "potential, and tapping into one's talents. The seed of potential has sprouted, and you are being called to take action and bring your intention to fruition"
CardsList[2].ArcanaMeaning = "spiritual enlightenment, inner illumination, divine knowledge and wisdom. Now is the time to be still so you can tune in to your intuition. The answers you are seeking will come from within, from your deepest truth and 'knowing'"
CardsList[3].ArcanaMeaning = "a strong connection with feminine aspects, such as elegance, sensuality, fertility, creative expression, and nurturing. You are in a period of growth, in which all you have dreamed of is now coming to fruition. Take a moment to reflect on the bounty that surrounds you and offer gratitude for all you have created so you can continue to build on this energy and create even more abundance in your life"
CardsList[4].ArcanaMeaning = "represents a powerful leader who demands respect and authority. Create calm out of chaos by breaking down any problem into its parts and then mapping out the actions you need to take to resolve it. Be systematic, strategic and highly organized in your approach, and stick to your plan until the end"
CardsList[5].ArcanaMeaning = "an established set of spiritual values and beliefs. You are being asked to commit to your practice in its most wholesome form – no customization, no adaptation, no bending the rules"
CardsList[6].ArcanaMeaning = "conscious connections and meaningful relationships. Your values system is being challenged, and you are being called to take the higher path, even if it is difficult. Do not carry out a decision based on fear or worry or guilt or shame. Now, more than ever, you must choose love – love for yourself, love for others and love for the Universe. Choose the best version of yourself"
CardsList[7].ArcanaMeaning = "willpower, determination, and strength. This is a sign of encouragemennt. Now isn’t the time to be passive in the hope that things will work out in your favor. Take focused action and stick to the course, no matter what challenges may come your way"
CardsList[8].ArcanaMeaning = "inner strength, and the determination to overcome any obstacle. Your strength gives you the confidence to overcome any growing fears, challenges or doubts. You have got what it takes to see this situation through to its eventual end"
CardsList[9].ArcanaMeaning = "inward reflection and introspection. When you allow yourself to tune in to your inner, guiding light, you will hear the answers you need and grow wise beyond your years"
CardsList[10].ArcanaMeaning = "good luck and a turning point. The wheel of fortune is always turning, and things in their present state will not last forever. Be willing to grow, and open to the help of others, as guidance from both the physical and spiritual realms is supporting you along your journey"
CardsList[11].ArcanaMeaning = "fairness, cause and effect, and law. You will need to make a choice that has the potential for long-term repercussions. Be ready to take responsibility for your actions and stand accountable for potential consequences"
CardsList[12].ArcanaMeaning = "surrender, letting go, and new perspectives. The universe is calling on you to release the old mental models and behavioural patterns that no longer serve you so you can see your world from a new perspective and embrace new opportunities that would have otherwise been hidden from you if you didn’t hit the brakes"
CardsList[13].ArcanaMeaning = "change, transformation, and transition. A major part of your life that is no longer serving you shall come to an end soon, opening up the possibility of something far more valuable and essential. You must close one door to open another"
CardsList[14].ArcanaMeaning = "balance, patience, and moderation. Remain calm, even when life feels stressful or frantic. Include others and bring together diverse groups of people to create harmony and cooperation. By working together, you will collectively leverage the right mix of talents, experiences, abilities and skills"
CardsList[15].ArcanaMeaning = "your darker side, and the negative forces that constrain you and hold you back from being the best version of yourself. See this as an opportunity to bring these negative influences into your conscious awareness, so you can then take action to free yourself from their hold. Shine your light on the negative patterns that have been standing in your way for so long, and over time, you will loosen the grip they have on you"
CardsList[16].ArcanaMeaning = "sudden change, chaos, and revelation. Change is coming, whether you would like it or not. A sudden event may bring about chaos and destruction in its wake. You have no choice but to surrender to the destruction and chaos, no matter how unwanted or painful. This destruction will allow new growth to emerge so your soul can evolve"
CardsList[17].ArcanaMeaning = "hope, purpose, and renewal. You are entering a peaceful, loving phase in your life, filled with calm energy, mental stability and more in-depth understanding of both yourself and others around you. This is a time of significant personal growth and development as you are now ready to receive the many blessings of the Universe"
CardsList[18].ArcanaMeaning = "illusion, fear, and anxiety. You need to listen to and trust your intuition so you can see beyond what is in front of you. Let go of your conscious mental blocks or negative self-talk and allow your intuition to guide you"
CardsList[19].ArcanaMeaning = "positivity, success, and fun. Through the challenges along your path, you discovered who you are and why you’re here. This is a sign that things are picking up, and that you are in a position where you can share your highest qualities and achievements with others"
CardsList[20].ArcanaMeaning = "rebirth, absolution, and inner calling. You are experiencing a spiritual awakening and realising that you are destined for so much more. You are close to reaching a significant stage in your journey. There will be others who have experienced something similar and who can show you the way to freedom from your troubles. Let them guide you and help you - rise together"
CardsList[21].ArcanaMeaning = "completion, accomplishment, and travel. Everything has come together, and you are in the right place, doing the right thing, achieving what you have envisioned. Look back at your past experiences and acknowledge how far you have come and what you learned along the way. It may surprise you to look back at your progress and see how much you achieved. This reflection may also be what you need to bring your project to its final stages"

def basic_spread():
    past_reading = random.choice(CardsList)
    present_reading = random.choice(CardsList)
    future_reading = random.choice(CardsList)
    reading = "Past: ", past_reading, "Present: ", present_reading, "Future: ", future_reading
    return str(reading)

def single_spread():
    reading = random.choice(CardsList)
    return str(reading)

print(str(basic_spread()))