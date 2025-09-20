import random
import os

Champs = {
    1: ["Aatrox", "Ezreal","Garen","Gnar","Kalista","Kayle","Kennen","Lucian","Malphite","Naafiri","Rell","Sivir","Syndra","Zac"],
    2: ["Dr. Mundo","Gangplank","Janna","Jhin","Kai'sa","Katarina","Kobuko","Lux","Rakan","Shen","Jax","Vi","Xayah","Xin Zhao"],
    3: ["Ahri","Caitlyn","Darius","Jayce","Lulu","Malzahar","Neeko","Senna","Swain","Udyr","Viego","Yasuo","Ziggs"],
    4: ["Akali","Ashe","Jarven IV","Jinx","Karma","K'sante","Leona","Poppy","Ryze","Samira","Sett","Volibear","Yuumi"],
    5: ["Braum","Gwen","Lee Sin","Seraphine","Twisted Fate","Varus","Yone","Zyra"]
}
Poolsize = {1: 30*len(Champs[1]), 2: 25*len(Champs[2]), 3:18*len(Champs[3]), 4:10*len(Champs[4]), 5:8*len(Champs[5])}