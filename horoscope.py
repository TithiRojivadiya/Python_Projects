import requests

sunsign = "leo"
day = "tomorrow"

def horoscope(sign,day):
    a = requests.get(f"http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/{day}").json()
    print(a.get('horoscope'))


horoscope(sunsign,day)

# {'sunsign': 'Libra',
#  'credit': '(c) Kelli Fox, The Astrologer, http://new.theastrologer.com',
#  'date': '2018-03-09', 'horoscope': "You feel the urge today to expand your horizons. This might happen through talking to people as you move through your daily business. Or perhaps you'll actually travel, or take up a new hobby. Studying new information is a great idea now. Your mind is like a sponge, ready to absorb facts and theories. So find a person or a subject that intrigues you, and dive into it.(c) Kelli Fox, The Astrologer, http://new.theastrologer.com",
#  'meta': {'mood': 'tolerant',
#           'keywords': 'unreserved, unrestrained',
#           'intensity': '59%'}}

