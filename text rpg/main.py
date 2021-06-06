import math
import time

import enemies
import players

print('Starting adventure... \n')

# ----------combat system-----------
def EnterCombat(player, enemy):
    print(f'An enemy', enemy['NAME'], 'appeared!')
    time.sleep(.7)
    while enemy['HP'] > 0 or player['HP'] > 0:
        print('What to do?')
        choice = input('[R]un [F]ight ').upper().strip()
        if choice == 'F' or choice == 'FIGHT':
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
        elif choice == 'R' or choice == 'RUN':
            print('You have escaped! \n')
            enemy['HP'] = enemy['MAXHP']
            break

        else:
            print('Choose a valid option! \n')

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

#-------------store------------------
def EnterStore(player):
	print('You entered the store \n')
	time.sleep(.8)
	print('Merchant: Greetings. How can I help you today?')
	while True:
		time.sleep(1)
		choice = input('[B]uy [S]ell [L]eave ').upper().strip()
		if choice == 'L' or choice == 'LEAVE':
			time.sleep(.8)
			print('Merchant: See you next time.\n')
			break
			
		if choice == 'B' or choice == 'BUY':
			time.sleep(.8)
			print('Which one of those items do you want to buy?\n')
			while True:
				time.sleep(.8)
				print('[1]Potion(20G)\n[2]Copper Sword\n[3]Leather Breastplate\n\n[0]Exit \n')
				time.sleep(.1)
				item = input('select the item ')
				if item == '0':
					time.sleep(.8)
					print('Merchant: Anything else?\n')
					break
				else:
					time.sleep(.8)
					print('Choose a valid option! \n')
				
		else:
			print('Choose a valid option!\n')


while True:
	LvlCheck(players.player)
	if players.player['HP'] > 0:
		print('You are in the city. What to do?')
		time.sleep(.5)
		choiceA = input('[A]dventure [S]tore ').upper().strip()
		if choiceA == 'A' or choiceA == 'ADVENTURE':
			time.sleep(.8)
			print('You went on an adventure! \n')
			EnterCombat(players.player, enemies.slime)
		if choiceA == 'S' or choiceA == 'STORE':
			EnterStore(players.player)
		else:
			print('Choose a valid option! \n')
	if players.player['HP'] <= 0:
		print('Game over')
		break