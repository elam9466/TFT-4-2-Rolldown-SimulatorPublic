import random
import os
from collections import Counter
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

def buyChamp(champ, pool, bench):
    if champ not in pool or pool[champ][1] <= 0:
        print(f"  Can't buy {champ}! Not in pool.")
        return False, pool, bench
    
    if len(bench) >= 9:
        print("  Bench is full!")
        return False, pool, bench
    
    cost, remaining = pool[champ]
    pool[champ] = (cost, remaining -1)
    bench.append(champ)

    bench = autoStarUp(bench)
    return True, pool, bench

def display_shop(cards):
    print("\nShop:")
    for i, card in enumerate(cards, start=1):
        print(f"  {i}. {card}")
    print()

def display_bench(bench):
    print("Bench:")
    if bench:
        for i, champ in enumerate(bench, start=1):
            print(f"  {i}. {champ}")
    else:
        print("  (empty)")
    print()

def starUp(bench):
    
    champ_counts = Counter(bench)
    nextStar = False
    
    for champ_name, count in champ_counts.items():
        if "***" in champ_name:  
            continue
            
        base_name = champ_name.replace(" **", "")  
        two_star_name = f"{base_name} **"
        
        two_star_count = bench.count(two_star_name)
        
        if two_star_count >= 3:
            for _ in range(3):
                bench.remove(two_star_name)
            
            three_star_name = f"{base_name} ***"
            bench.append(three_star_name)
            print(f"{base_name} into 3-star {base_name}")
            nextStar = True
    
    champ_counts = Counter([champ.replace(" **", "").replace(" ***", "") for champ in bench])
    
    for base_name, count in champ_counts.items():
        if count >= 3:
            one_star_count = sum(1 for champ in bench if champ == base_name)
            
            if one_star_count >= 3:
                for _ in range(3):
                    bench.remove(base_name)
                
                two_star_name = f"{base_name} **"
                bench.append(two_star_name)
                print(f"{base_name} into 2-star {base_name}")
                any_combinations = True
    
    if nextStar:
        bench, multipleStarup = starUp(bench)
        nextStar = nextStar or multipleStarup
    
    return bench, nextStar


def autoStarUp(bench):
    bench, autoStar = starUp(bench)
    return bench



