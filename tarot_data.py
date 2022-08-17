MajorArcana = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Justice", "The Hermit", "Wheel of Fortune", "Strength", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World", "The Fool (Reversed)", "The Magician (Reversed)", "The High Priestess (Reversed)", "The Empress (Reversed)", "The Emperor (Reversed)", "The Hierophant (Reversed)", "The Lovers (Reversed)", "The Chariot (Reversed)", "Justice (Reversed)", "The Hermit (Reversed)", "Wheel of Fortune (Reversed)", "Strength (Reversed)", "The Hanged Man (Reversed)", "Death (Reversed)", "Temperance (Reversed)", "The Devil (Reversed)", "The Tower (Reversed)", "The Star (Reversed)", "The Moon (Reversed)", "The Sun (Reversed)", "Judgement (Reversed)", "The World (Reversed)"]
MinorArcana = ["Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups", "Five of Cups", "Six of Cups", "Seven of Cups", "Eight of Cups", "Nine of Cups", "Ten of Cups", "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups", "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords", "Five of Swords", "Six of Swords", "Seven of Swords", "Eight of Swords", "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords", "Ace of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles", "Five of Pentacles", "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles", "Nine of Pentacles", "Ten of Pentacles", "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles", "Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands", "Five of Wands", "Six of Wands", "Seven of Wands", "Eight of Wands", "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands", "Queen of Wands", "King of Wands"]
class TarotCard:
    def __init__(self, MajorArcana, MinorArcana="None"):
        self.MajorArcana = MajorArcana
        self.MinorArcana = MinorArcana
        self.ArcanaMeaning = ""
    def __repr__(self):
        return "{arcana} represents {meaning}.".format(arcana=self.MajorArcana, meaning=self.ArcanaMeaning)

# Tarot Reading Interpretations, info obtained from https://www.biddytarot.com/tarot-card-meanings/major-arcana/
MajArcana = [TarotCard(_) for _ in MajorArcana]
MinArcana = [TarotCard(_) for _ in MinorArcana]
MajArcana[0].ArcanaMeaning = "new beginnings, opportunity, and potential. Throw caution to the wind and be ready to embrace the unknown, leaving behind any fear, worry or anxiety about what may or may not happen"
MajArcana[1].ArcanaMeaning = "potential, and tapping into one's talents. The seed of potential has sprouted, and you are being called to take action and bring your intention to fruition"
MajArcana[2].ArcanaMeaning = "spiritual enlightenment, inner illumination, divine knowledge and wisdom. Now is the time to be still so you can tune in to your intuition. The answers you are seeking will come from within, from your deepest truth and 'knowing'"
MajArcana[3].ArcanaMeaning = "a strong connection with feminine aspects, such as elegance, sensuality, fertility, creative expression, and nurturing. You are in a period of growth, in which all you have dreamed of is now coming to fruition. Take a moment to reflect on the bounty that surrounds you and offer gratitude for all you have created so you can continue to build on this energy and create even more abundance in your life"
MajArcana[4].ArcanaMeaning = "represents a powerful leader who demands respect and authority. Create calm out of chaos by breaking down any problem into its parts and then mapping out the actions you need to take to resolve it. Be systematic, strategic and highly organized in your approach, and stick to your plan until the end"
MajArcana[5].ArcanaMeaning = "an established set of spiritual values and beliefs. You are being asked to commit to your practice in its most wholesome form – no customization, no adaptation, no bending the rules"
MajArcana[6].ArcanaMeaning = "conscious connections and meaningful relationships. Your values system is being challenged, and you are being called to take the higher path, even if it is difficult. Do not carry out a decision based on fear or worry or guilt or shame. Now, more than ever, you must choose love – love for yourself, love for others and love for the Universe. Choose the best version of yourself"
MajArcana[7].ArcanaMeaning = "willpower, determination, and strength. This is a sign of encouragemennt. Now isn’t the time to be passive in the hope that things will work out in your favor. Take focused action and stick to the course, no matter what challenges may come your way"
MajArcana[8].ArcanaMeaning = "inner strength, and the determination to overcome any obstacle. Your strength gives you the confidence to overcome any growing fears, challenges or doubts. You have got what it takes to see this situation through to its eventual end"
MajArcana[9].ArcanaMeaning = "inward reflection and introspection. When you allow yourself to tune in to your inner, guiding light, you will hear the answers you need and grow wise beyond your years"
MajArcana[10].ArcanaMeaning = "good luck and a turning point. The wheel of fortune is always turning, and things in their present state will not last forever. Be willing to grow, and open to the help of others, as guidance from both the physical and spiritual realms is supporting you along your journey"
MajArcana[11].ArcanaMeaning = "fairness, cause and effect, and law. You will need to make a choice that has the potential for long-term repercussions. Be ready to take responsibility for your actions and stand accountable for potential consequences"
MajArcana[12].ArcanaMeaning = "surrender, letting go, and new perspectives. The universe is calling on you to release the old mental models and behavioural patterns that no longer serve you so you can see your world from a new perspective and embrace new opportunities that would have otherwise been hidden from you if you didn’t hit the brakes"
MajArcana[13].ArcanaMeaning = "change, transformation, and transition. A major part of your life that is no longer serving you shall come to an end soon, opening up the possibility of something far more valuable and essential. You must close one door to open another"
MajArcana[14].ArcanaMeaning = "balance, patience, and moderation. Remain calm, even when life feels stressful or frantic. Include others and bring together diverse groups of people to create harmony and cooperation. By working together, you will collectively leverage the right mix of talents, experiences, abilities and skills"
MajArcana[15].ArcanaMeaning = "your darker side, and the negative forces that constrain you and hold you back from being the best version of yourself. See this as an opportunity to bring these negative influences into your conscious awareness, so you can then take action to free yourself from their hold. Shine your light on the negative patterns that have been standing in your way for so long, and over time, you will loosen the grip they have on you"
MajArcana[16].ArcanaMeaning = "sudden change, chaos, and revelation. Change is coming, whether you would like it or not. A sudden event may bring about chaos and destruction in its wake. You have no choice but to surrender to the destruction and chaos, no matter how unwanted or painful. This destruction will allow new growth to emerge so your soul can evolve"
MajArcana[17].ArcanaMeaning = "hope, purpose, and renewal. You are entering a peaceful, loving phase in your life, filled with calm energy, mental stability and more in-depth understanding of both yourself and others around you. This is a time of significant personal growth and development as you are now ready to receive the many blessings of the Universe"
MajArcana[18].ArcanaMeaning = "illusion, fear, and anxiety. You need to listen to and trust your intuition so you can see beyond what is in front of you. Let go of your conscious mental blocks or negative self-talk and allow your intuition to guide you"
MajArcana[19].ArcanaMeaning = "positivity, success, and fun. Through the challenges along your path, you discovered who you are and why you’re here. This is a sign that things are picking up, and that you are in a position where you can share your highest qualities and achievements with others"
MajArcana[20].ArcanaMeaning = "rebirth, absolution, and inner calling. You are experiencing a spiritual awakening and realising that you are destined for so much more. You are close to reaching a significant stage in your journey. There will be others who have experienced something similar and who can show you the way to freedom from your troubles. Let them guide you and help you - rise together"
MajArcana[21].ArcanaMeaning = "completion, accomplishment, and travel. Everything has come together, and you are in the right place, doing the right thing, achieving what you have envisioned. Look back at your past experiences and acknowledge how far you have come and what you learned along the way. It may surprise you to look back at your progress and see how much you achieved. This reflection may also be what you need to bring your project to its final stages"
MajArcana[22].ArcanaMeaning = "holding back, recklessness, and risk-taking. This suggests that you have conceived of a new project but aren’t ready to ‘birth’ it into the world just yet. You may worry that you are not fit or that you don’t have all the tools, skills and resources you need to make this project a success. Something is holding you back, and you are preventing yourself from moving forward"
MajArcana[23].ArcanaMeaning = "manipulation, poor planning, and untapped talents. On one level, you are exploring what you wish to manifest, but are not taking the steps forward to achieve your goal.  You may worry that you do not have the right tools or resources you need. If you take care of what you intend to manifest, the Universe will work out the how. Stay attuned to your intuition and pay attention to opportunities as they arise"
MajArcana[24].ArcanaMeaning = "secrets, disconnect from intuition, and withdrawal. Be still and direct your attention inward to listen to your voice and wisdom. You may be swayed by other people’s opinions or swept up in their drama when what you really need to do is focus on what is right for you"
MajArcana[25].ArcanaMeaning = "creative block and dependence on others. Make self-love and self-care a priority. Now is the time to bring your loving energy and focus to yourself, especially if you have been giving away your personal power by placing too much emphasis on another person’s emotional or material needs, thus neglecting your own. You may also crave a stronger connection with nature and Mother Earth. Now is the perfect occasion to spend even just a few hours in a natural setting such as a beach, park or garden"
MajArcana[26].ArcanaMeaning = "excessive control, lack of discipline, and inflexibility. This can suggest an over-use and abuse of authoritative power surrounding you. It could originate from you or from another person, often a boss, partner or father figure. Seek to find a solution where you lead from a place of personal power and enable others to do the same. Power can be equally and constructively distributed – you don’t need to take it from others, nor do you need to give yours away"
MajArcana[27].ArcanaMeaning = "personal beliefs, freedom, and challenging the status quo. The Universe wishes to remind you that you are your own teacher. You are being guided to follow your own path and adopt your own spiritual belief systems rather than blindly following others’. It may feel unsettling at first as you make your own way, but over time, you will learn to trust yourself and tap into your inner knowledge"
MajArcana[28].ArcanaMeaning = "self-love, imbalance, and misalignment of values. This can signal a time when you’re out of sync with those around you, particularly your loved ones. You may find your relationships are strained and communication is challenging. Come back to the reason you have them in your life. If you love them unconditionally, know this moment shall pass and the best you can do is bring love and compassion to the situation. In other cases, you may realise that you have simply grown apart and it’s time to move on"
MajArcana[29].ArcanaMeaning = "self-discipline, opposition, and lack of direction. You might bang your head against a brick wall, trying to push a project forward when really, you ought to back off or change direction. Or you might have lost your motivation and no longer feel as committed to the outcome as you did when you started. This is a warning that you are letting obstacles and challenges get in the way, preventing you from achieving what you set out to do. It’s all getting too hard, and you don’t have the will to go on. If that resonates, stop for a moment and think about the things that matter most to you and why you want to achieve this goal"
MajArcana[30].ArcanaMeaning = "low energy, self-doubt, and raw emotion. Tune in to your current levels of inner strength, confidence and self-belief. If you have recently experienced a setback, you may be vulnerable and lacking in self-confidence.  Know that your core strength will always be with you and now is as good a time as any to reconnect with this power.  You may hold more strength and resilience than you give yourself credit for - so be kind to yourself."
MajArcana[31].ArcanaMeaning = "isolation, loneliness, and withdrawal. This can go one of two ways: either you ar enot taking enough time for personal reflection, or you are taking too much time. It is time to go deeper into your inner being and rediscover your greater purpose on this earth. You may have been so busy dealing with day-to-day issues that you have forgotten to listen to your inner voice. On the other hand, you may have been spending too much time reflecting on your inner self. This suggests that you may be taking this isolation thing too far. Do not underestimate the value of staying connected with others, even while you are going through your journey. Be mindful of other peoples' needs as well, though, as you do not want to become so absorbed in yourself and your personal dilemmas that you shut out your family and friends"
MajArcana[32].ArcanaMeaning = "bad luck, resistance to change, and breaking cycles. Your luck and fortune may take a turn for the worst. You may experience unexpected change or negative forces could be at play, leaving you helpless.  You can either do nothing and hope things will get better, or you can act to improve your situation. See this moment as an opportunity to take control of your destiny in order to get your life back on track. This could also suggest that change has become a source of significant stress, and you may be trying to consciously or subconsciously stop events from running their course. Accept that change is inevitable and you will have a much-improved experience"
MajArcana[33].ArcanaMeaning = "unfairness, lack of accountability, and dishonesty. Internally, you may know you've done something that isn't morally right. Others may not see it yet, so you have a choice: hide it and hope no one finds out, or own up to your mistakes and take focused action to resolve the situation. You are being dishonest with yourself and others, and your unwillingness to look beyond your own fears and ego blinds you to the broader lesson. Acknowledge where you made a mistake and do whatever you can to make it right. In doing so, you will free yourself from any guilt or shame and empower yourself to make better decisions."
MajArcana[34].ArcanaMeaning = "delays, resistance, and indecision. You need to pause and see things from a different perspective, even though you are resisting it. Your spirit and body are asking you to slow down, but your mind keeps racing. You must rest before it's too late, and you end up crashing. If your life has already been on pause for a period, this may come as a positive sign that you can now move forward with a new perspective and a renewed sense of energy"
MajArcana[35].ArcanaMeaning = "resistance to change, inner purging, and personal transformation. You are on the verge of meaningful change, but you are resisting it. Maybe you are reluctant to let go, or you may not know how to make the change you need. Because of your refusal, life has stagnated, and you feel stuck in limbo. As you learn to release the past and surrender to the present, the future becomes even brighter. Be sure to embrace change in all forms, and you may be surprised at how this subtle shift in energy allows new doors to open in ways you may never have expected"
MajArcana[36].ArcanaMeaning = "imbalance, excess, and self-healing. This is a sign to restore balance and moderation as soon as possible. Perhaps you have been doing something in excess. This activity will take you further away from who you are and what you are here to do. Remember, everything is fine in moderation. This can also be a sign that something is off in your life, creating stress and tension. You can ignore it and carry on with life as usual, but if you stay in this state for too long, that voice will just get louder and louder until you're forced to pay attention"
MajArcana[37].ArcanaMeaning = "exploring dark thoughts and detachment. This often appears when you are on the verge of a breakthrough. You are being called to your highest potential, but first ,you must let go of any unhealthy attachments or limiting beliefs that may hold you back. This calls on you to confront your inner fears and anxieties to free yourself from the chains that bind you to your limiting beliefs and unhealthy attachments"
MajArcana[38].ArcanaMeaning = "personal transformation, fear of change, and averting disaster. This suggests that you are undergoing a significant personal transformation and upheaval. This change is something you are instigating, and is calling into question your fundamental belief systems, values, purpose, and meaning. This can also be a sign that you're resisting change and delaying the necessary destruction and upheaval. You may be in denial that change is occurring, or you may be clinging to an old belief system even though you know it is no longer relevant or healthy for you"
MajArcana[39].ArcanaMeaning = "lack of faith, despair, and disconnection. This can mean that you have lost faith and hope in the Universe. You may feel overwhelmed by life's challeneges right now, and may be questioning why you are being put through this. Take a moment to ask yourself how your experiences could be a blessing, and not a punishment. This could be a sign that you are disengaged and uninspired with life or components of your life - such as work, hobbies, relationships, etc. Reconnect to what is truly important to you and your purpose for this lifetime"
MajArcana[40].ArcanaMeaning = "repressed emotion and inner confusion. This indicates that you have been dealing with fears and anxiety, and now the negative influences of these energies are subsiding. You may bury these feelings even deeper within your subconscious so you can avoid your dark shadows. You may not be ready to face your emotions, pushing them to the side and pretending as if nothing is wrong. This could work in the short term, but eventually you will need to resurface these emotions and deal with them head on"
MajArcana[41].ArcanaMeaning = "feeling down or overly optimistic. See this as your permission slip to leave behind your work and responsibilities, even for just a moment, and enjoy life. You could dance, sing, and let your heart be free. You may be struggling to see the bright side of life. You may have experienced setbacks that damaged your enthusiasm and optimism, and perhaps led you to question whether you cna achieve what you set out to do. Nonetheless, this is only temporary. Obstacles you see can easily be removed if you put your mind to it. It may just take a bit more effort than usual"
MajArcana[42].ArcanaMeaning = "self-doubt and your inner critic. This calls for a period of reflection and self-evaluation. You may arrive at a deep understanding of the universal themes weaving throughout your life and what you can do or change to avoid these situations. To clear these past mistakes and regrets, and any associated guilt or shame, you must work on self-forgiveness, self-love, and release. Maybe you're afraid of the sacrifice you'll need to make to achieve your goal, or you're worrie you are not ready to step into a more prominent role and just want to play it safe. It's time to push back your inner fears and self-doubt, and trust that the Universe has your back"
MajArcana[43].ArcanaMeaning = "shortcuts, delays, and seeking personal closure. Perhaps you are still emotionally attached to a past relationship and want to move on, or you dream of the person you once were. You know, deep down, that in order to accept and embrace where you are now, you need to let go of the past and move on. This can signify that you want to fulfill a big goal or complet e a big project, but you're not taking all the steps necessary to get there, opting for the easiest or quickest path to attain your goal. This will not lead to the outcome you intend. You need to experience the trials and tribulations along the way, so you can learn and grow."

MinArcana[0].ArcanaMeaning = "love, new relationships, compassion, and creativity. Now is the perfect time for you to open your heart and experience the rich flow of emotion available to you right now. This is an invitation to be open to creative expression, especially when you can allow your emotions to shine through your endeavours. You may be inspired to start a new project or learn something new. Let your imagination and talent unfurl to new possibilities"
MinArcana[1].ArcanaMeaning = "unified love, partnership, and mutual attraction. This shows you are creating deep connections and partnerships based on shared values, compassion, and unconditional love. While these relationships may still be in the early stages, they have the potential to grow and develop into something deeply fulfilling and rewarding in the long-term"
MinArcana[2].ArcanaMeaning = "celebration, friendship, creativity, and collaborations."
MinArcana[3].ArcanaMeaning = ""
MinArcana[4].ArcanaMeaning = ""
MinArcana[5].ArcanaMeaning = ""
MinArcana[6].ArcanaMeaning = ""
MinArcana[7].ArcanaMeaning = ""
MinArcana[8].ArcanaMeaning = ""
MinArcana[9].ArcanaMeaning = ""
MinArcana[10].ArcanaMeaning = ""
MinArcana[11].ArcanaMeaning = ""
MinArcana[12].ArcanaMeaning = ""
MinArcana[13].ArcanaMeaning = ""
MinArcana[14].ArcanaMeaning = ""
MinArcana[15].ArcanaMeaning = ""
MinArcana[16].ArcanaMeaning = ""
MinArcana[17].ArcanaMeaning = ""
MinArcana[18].ArcanaMeaning = ""
MinArcana[19].ArcanaMeaning = ""
MinArcana[20].ArcanaMeaning = ""
MinArcana[21].ArcanaMeaning = ""
MinArcana[22].ArcanaMeaning = ""
MinArcana[23].ArcanaMeaning = ""
MinArcana[24].ArcanaMeaning = ""
MinArcana[25].ArcanaMeaning = ""
MinArcana[26].ArcanaMeaning = ""
MinArcana[27].ArcanaMeaning = ""
MinArcana[28].ArcanaMeaning = ""
MinArcana[29].ArcanaMeaning = ""
MinArcana[30].ArcanaMeaning = ""
MinArcana[31].ArcanaMeaning = ""
MinArcana[32].ArcanaMeaning = ""
MinArcana[33].ArcanaMeaning = ""
MinArcana[34].ArcanaMeaning = ""
MinArcana[35].ArcanaMeaning = ""
MinArcana[36].ArcanaMeaning = ""
MinArcana[37].ArcanaMeaning = ""
MinArcana[38].ArcanaMeaning = ""
MinArcana[39].ArcanaMeaning = ""
MinArcana[40].ArcanaMeaning = ""
MinArcana[41].ArcanaMeaning = ""
MinArcana[42].ArcanaMeaning = ""
MinArcana[43].ArcanaMeaning = ""
MinArcana[44].ArcanaMeaning = ""
MinArcana[45].ArcanaMeaning = ""
MinArcana[46].ArcanaMeaning = ""
MinArcana[47].ArcanaMeaning = ""
MinArcana[48].ArcanaMeaning = ""
MinArcana[49].ArcanaMeaning = ""
MinArcana[50].ArcanaMeaning = ""
MinArcana[51].ArcanaMeaning = ""
MinArcana[52].ArcanaMeaning = ""
MinArcana[53].ArcanaMeaning = ""
MinArcana[54].ArcanaMeaning = ""
MinArcana[55].ArcanaMeaning = ""
