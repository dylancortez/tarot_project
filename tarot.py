
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
CardsList[3].ArcanaMeaning = "the germination of an idea before it is ready to be born, and the need to be receptive to change"
CardsList[4].ArcanaMeaning = "stability, power, and logic"
CardsList[5].ArcanaMeaning =
CardsList[6].ArcanaMeaning =
CardsList[7].ArcanaMeaning =
CardsList[8].ArcanaMeaning =
CardsList[9].ArcanaMeaning =
CardsList[10].ArcanaMeaning =
CardsList[11].ArcanaMeaning = 
CardsList[12].ArcanaMeaning =
CardsList[13].ArcanaMeaning =
CardsList[14].ArcanaMeaning =
CardsList[15].ArcanaMeaning =
CardsList[16].ArcanaMeaning =
CardsList[17].ArcanaMeaning =
CardsList[18].ArcanaMeaning =
CardsList[19].ArcanaMeaning =
CardsList[20].ArcanaMeaning =
CardsList[21].ArcanaMeaning =