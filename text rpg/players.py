import items
i = items

equipped = {
    'sword': i.wooden_sword,
    'shield': '',
    'breastplate': '',
    'helmet' : '',
    'greaves': '',
    'gauntlet': '',
    'shoes': '',
}

player = {
    'MAXHP': 100,
    'HP': 100,
    'ATK': 25,
    'SPE': 15,
    'LVL': 1,
    'XP': 0,
    'G': 100,
}


DMG = player['ATK'] + equipped['sword']['ATK']



