import math
import time

import items 
import enemies
import players

i = items

print('Starting adventure... \n')

# ----------combat system-----------
def EnterCombat(player, enemy):
    print(f'An enemy', enemy['NAME'], 'appeared!')
    time.sleep(.7)
    while True:
        print('What to do?')
        choice = input('[R]un\n[F]ight\n\n-').upper().strip()
        if choice == 'F':
            time.sleep(.8)
            print('You chose to fight \n')         
            if player['SPE'] > enemy['SPE']:
                enemy['HP'] -= player['ATK']
                player['HP'] -= enemy['ATK']
                print(f'Enemy', enemy['NAME'], 'took', player['ATK'], f'damage! \n')
                time.sleep(.8)
                print('You took', enemy['ATK'], 'damage! \n')
                time.sleep(.8)
                if enemy['HP'] > 0:
                    print('Your HP:', player['HP'])
                    print('Enemy HP:', enemy['HP'])
                    time.sleep(.5)
                if enemy['HP'] <= 0:
                    print('Enemy died! \n')
                    time.sleep(.8)
                    player['XP'] += enemy['XP']
                    player['G'] += enemy['G']
                    
                    print('You won', enemy['XP'], 'XP and', enemy['G'], 'gold! \n')
                    time.sleep(.8)
                    
                    LvlCheck(players.player)    
                if player['HP'] <= 0:
                	print('you died! \n')
            if enemy['HP'] <= 0 or player['HP'] <= 0:
                enemy['HP'] = enemy['MAXHP']  
                break
        elif choice == 'R':
            print('You have escaped! \n')
            enemy['HP'] = enemy['MAXHP']
            break

        else:
            print('Choose a valid option!\n')
            time.sleep(.8)

#----------level up system--------------
def LevelUp(player, level):
	player['LVL'] += level
	player['MAXHP'] += 3 * level
	player['ATK'] += 2 * level
	player['SPE'] += 1 * level
	print('Level up! Level:', player['LVL'])
	
def LvlCheck(player):
	if player['XP'] >= math.pow(player['LVL'], 1.12) * 100:
		LevelUp(players.player, 1)

#----------changing equipment---------
def ChangeSword():
    if players.equipped['sword'] == i.wooden_sword:
        players.equipped['sword'] = i.copper_sword
        players.DMG = players.player['ATK'] + players.equipped['sword']['ATK']
    elif players.equipped['sword'] == i.copper_sword:
        players.equipped['sword'] = i.wooden_sword
        players.DMG = players.player['ATK'] + players.equipped['sword']['ATK']
    

#-------------store------------------
def EnterStore(player):
    print('You entered the store \n')
    time.sleep(.8)
    print('Merchant: Greetings. How can I help you today?\n')
    while True:
        time.sleep(1)
        choiceB = input('[B]uy\n[S]ell\n[L]eave\n\n-').upper().strip()
        if choiceB == 'L':
            time.sleep(.8)
            print('Merchant: See you next time.\n')
            break
			
        elif choiceB == 'B':
            time.sleep(.8)
            print('Which one of those items do you want to buy?\n')
            while True:
                time.sleep(.8)
                print('*You have:', player['G'],'G\n')
                print('[1]', i.potion['NAME'], i.potion['BPRICE'], 'G      --', i.potion['DESC'])
                print('[2]', i.copper_sword['NAME'], i.copper_sword['BPRICE'], 'G      --', i.copper_sword['DESC'])
                print('[3]', i.lather_breastplate['NAME'], i.lather_breastplate['BPRICE'], 'G      --', i.lather_breastplate['DESC'])
                print('\n[0] Exit \n')
                time.sleep(.1)
                item = input('select the item ')
                if item == '0':
                    time.sleep(.8)
                    print('Merchant: Anything else?\n')
                    break
                elif item == '1':
                    if player['G'] >= i.potion['BPRICE']:
                        time.sleep(.8)
                        player['G'] -= i.potion['BPRICE']
                        print('Merchant: There is.')
                        time.sleep(.8)
                        print('Merchant: Anything else?\n')
                    else:
                        print('Merchant: You do not have enough money.\n')
                elif item == '2':
                    if player['G'] >= i.copper_sword['BPRICE']:
                        time.sleep(.8)
                        player['G'] -= i.copper_sword['BPRICE']
                        print('Merchant: There is.')
                        time.sleep(.8)
                        print('Merchant: Anything else?\n')
                    else:
                        print('Merchant: You do not have enough money.\n')
                elif item == '3':
                    if player['G'] >= i.lather_breastplate['BPRICE']:
                        time.sleep(.8)
                        player['G'] -= i.lather_breastplate['BPRICE']
                        print('Merchant: There is.')
                        time.sleep(.8)
                        print('Merchant: Anything else?\n')
                    else:
                        print('Merchant: You do not have enough money.\n')
                else:
                    time.sleep(.8)
                    print('Choose a valid option! \n')
				
        else:
            print('Choose a valid option!\n')


while True:
    LvlCheck(players.player)
    if players.player['HP'] > 0:
        print('You are in the city. What to do?')
        print(players.DMG)
        time.sleep(.5)
        choiceA = input('[A]dventure\n[S]tore\n\n-').upper().strip()
        if choiceA == 'A':
            time.sleep(.8)
            print('You went on an adventure! \n')
            EnterCombat(players.player, enemies.slime)
        elif choiceA == 'S':
            EnterStore(players.player)
        else:
            print('Choose a valid option!\n')
    if players.player['HP'] <= 0:
        print('Game over')
        break