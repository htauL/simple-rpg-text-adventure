import math

import enemies
import players

print('starting adventure... \n')

# ----------combat system-----------
def EnterCombat(player, enemy):
    print(f'An enemy', enemy['NAME'], 'appeared!')
    while enemy['HP'] > 0 or player['HP'] > 0:
        print('What to do?')
        choice = input('[R]un [F]ight ').upper().strip()
        if choice == 'F' or choice == 'FIGHT':
            print('You chose to fight \n')         
            if player['SPE'] > enemy['SPE']:
                enemy['HP'] -= player['ATK']
                player['HP'] -= enemy['ATK']
                print(f'Enemy', enemy['NAME'], 'took', player['ATK'], f'damage! \n')
                print('You took', enemy['ATK'], 'damage! \n')
                if enemy['HP'] > 0:
                    print('Your HP:', player['HP'])
                    print('Enemy HP:', enemy['HP'])
                if enemy['HP'] <= 0:
                    print('Enemy died! \n')
                    player['XP'] += enemy['XP']
                    player['G'] += enemy['G']
                    
                    print('You won', enemy['XP'], 'XP and', enemy['G'], 'gold! \n')
                    
                    LvlCheck(players.player)    
                if player['HP'] <= 0:
                	print('you died! \n')
            if enemy['HP'] <= 0 or player['HP'] <= 0:
                enemy['HP'] = enemy['MAXHP']  
                break
        elif choice == 'R' or choice == 'RUN':
            print('You have escaped!')
            enemy['HP'] = enemy['MAXHP']
            break

        else:
            print('Choose a valid option! \n')

#----------level up system------------x
def LevelUp(player, level):
	player['LVL'] += level
	player['MAXHP'] += 3 * level
	player['ATK'] += 2 * level
	player['SPE'] += 1 * level
	print('Level up! Level:', player['LVL'])
	
def LvlCheck(player):
	if player['XP'] >= math.pow(player['LVL'], 1.12) * 100:
		LevelUp(players.player, 1)
	
while True:
	LvlCheck(players.player)
	if players.player['HP'] > 0:
		print('You are in the city. What to do?')
		choice = input('[A]dventure ').upper().strip()
		if choice == 'A' or choice == 'ADVENTURE':
			print('You went on an adventure! \n')
			EnterCombat(players.player, enemies.slime)
		else:
			print('Choose a valid option! \n')
	if players.player['HP'] <= 0:
		print('Game over')
		break