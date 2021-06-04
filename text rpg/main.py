import enemies
import players

print('starting adventure...')

# ----------combat system-----------
def EnterCombat(player, enemy):
    print(f'An enemy', enemy['NAME'], 'appeared!')
    while enemy['HP'] > 0 or player['HP'] > 0:
        print('What to do?')
        choice = input('[R]un [F]ight ').upper().strip()
        if choice == 'F':
            print('You chose to fight')         
            if player['SPE'] > enemy['SPE']:
                enemy['HP'] -= player['ATK']
                print(f'Enemy', enemy['NAME'], 'took', player['ATK'], f'damage!')
                if enemy['HP'] > 0:
                    print('Enemy HP:', enemy['HP'])
                if enemy['HP'] <= 0:
                    print('Enemy died!')
            if enemy['HP'] <= 0:           
                break
        elif choice == 'R':
            print('You have escaped!')
            break

        elif choice != 'R' or 'F':
            print('Choose a valid option!')

EnterCombat(players.player, enemies.slime)