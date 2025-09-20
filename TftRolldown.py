import random
import os

Champs = {
    "Aatrox": (1,30) , "Ezreal": (1,30),"Garen": (1,30),"Gnar": (1,30),"Kalista": (1,30),"Kayle": (1,30),"Kennen": (1,30),"Lucian": (1,30),"Malphite": (1,30),"Naafiri": (1,30),"Rell": (1,30),"Sivir": (1,30),"Syndra": (1,30),"Zac": (1,30),
    
    "Dr. Mundo": (2,25),"Gangplank": (2,25),"Janna": (2,25),"Jhin": (2,25),"Kai'sa": (2,25),"Katarina": (2,25),"Kobuko": (2,25),"Lux": (2,25),"Rakan": (2,25),"Shen": (2,25),"Jax": (2,25),"Vi": (2,25),"Xayah": (2,25),"Xin Zhao": (2,25),
    
    "Ahri": (3,18),"Caitlyn": (3,18),"Darius": (3,18),"Jayce": (3,18),"Lulu": (3,18),"Malzahar": (3,18),"Neeko": (3,18),"Senna": (3,18),"Swain": (3,18),"Udyr": (3,18),"Viego": (3,18),"Yasuo": (3,18),"Ziggs": (3,18),
    
    "Akali":(4,10),"Ashe":(4,10),"Jarven IV":(4,10),"Jinx":(4,10),"Karma":(4,10),"K'sante":(4,10),"Leona":(4,10),"Poppy":(4,10),"Ryze":(4,10),"Samira":(4,10),"Sett":(4,10),"Volibear":(4,10),"Yuumi":(4,10),
    
    "Braum": (5,9),"Gwen": (5,9),"Lee Sin": (5,9),"Seraphine": (5,9),"Twisted Fate": (5,9),"Varus": (5,9),"Yone": (5,9),"Zyra": (5,9)
}

RollingOdds = [0.17, 0.24, 0.32, 0.24, 0.03]
currentPool = Champs.copy()
def shop(currentPool, odds):
    cards = []
    for i in range (5):
        chosenCost = random.choices([1,2,3,4,5], weights = odds, k=1)[0]

        availableChamps = []
        for champ, (cost, remaining) in currentPool.items():
            if cost == chosenCost and remaining > 0:
                availableChamps.append(champ)
        if availableChamps:
            chosenChamp = random.choice(availableChamps)
            cards.append(chosenChamp)
            cost, remaining = currentPool[chosenChamp]
            currentPool[chosenChamp] = (cost, remaining -1)
        else:
            cards.append("-----")
    return cards

