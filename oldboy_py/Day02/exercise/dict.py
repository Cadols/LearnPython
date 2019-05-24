#!/usr/bin/env python
# -*- coding: utf-8 -*-

dict = {
    'Europe': {
        'UbiSoft': 'AssassinCreed',
        'Supercell': 'ClashOfClans'
    },
    'Japan': {
        'Nintendo': 'FireEmblem',
        'Capcom': 'BioHazard',
        'SquareEnix': 'FinalFantasy'
    },
    'U.S.A': {
        'Blizzard': 'WarCraft',
        'E.A': 'TheNeedForSpeed'
    }
}

print(dict)

dict['Japan']['SquareEnix'] = 'DragonQuest'
print(dict)

dict['U.S.A']['EpicGames'] = 'WarGear'
print(dict)

dict2 = {
    'Japan': {
        'Capcom': 'StreetFighter'
    },
    'One': 1,
    'Two': 2
}