import time, os, shutil, random, msvcrt, sys, colorama
from getch import getch, pause
from colorama import Fore, Style


def deleteScreen():
	os.system('cls')
def printMainMenu():
	print (" ______________________________________________________ ".center(shutil.get_terminal_size().columns))
	print ("|                                                      |".center(shutil.get_terminal_size().columns))
	print ("|                                                      |".center(shutil.get_terminal_size().columns))
	print ("|                  Word slaying game                   |".center(shutil.get_terminal_size().columns))
	print ("|                                                      |".center(shutil.get_terminal_size().columns))
	print ("|______________________________________________________|".center(shutil.get_terminal_size().columns))
	print ("|                                                      |".center(shutil.get_terminal_size().columns))
	print ("|                                                      |".center(shutil.get_terminal_size().columns))
	print ("|       Start New Game (S)          Load Level (L)     |".center(shutil.get_terminal_size().columns))
	print ("|                                                      |".center(shutil.get_terminal_size().columns))
	print ("|                                                      |".center(shutil.get_terminal_size().columns))
	print ("|                                                      |".center(shutil.get_terminal_size().columns))
	print ("|       Exit  (E)                   Help      (H)      |".center(shutil.get_terminal_size().columns))
	print ("|                                                      |".center(shutil.get_terminal_size().columns))
	print (" \____________________________________________________/ ".center(shutil.get_terminal_size().columns))
def printGameOver():
	print ("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀".center(shutil.get_terminal_size().columns))
	print ("██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼".center(shutil.get_terminal_size().columns))
	print ("██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀".center(shutil.get_terminal_size().columns))
	print ("██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼".center(shutil.get_terminal_size().columns))
	print ("███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼".center(shutil.get_terminal_size().columns))
	print ("██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼".center(shutil.get_terminal_size().columns))
	print ("██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼".center(shutil.get_terminal_size().columns))
	print ("██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼".center(shutil.get_terminal_size().columns))
	print ("███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼".center(shutil.get_terminal_size().columns))
	print ("           Main Menu (M)            ".center(shutil.get_terminal_size().columns))
	print ("             Retry (R)              ".center(shutil.get_terminal_size().columns))
def printWin():
	print ("__     __                               ".center(shutil.get_terminal_size().columns))
	print ("\ \   / /                               ".center(shutil.get_terminal_size().columns))
	print (" \ \_/ /__  _   _  __      _____  _ __  ".center(shutil.get_terminal_size().columns))
	print ("  \   / _ \| | | | \ \ /\ / / _ \| '_ \ ".center(shutil.get_terminal_size().columns))
	print ("   | | (_) | |_| |  \ V  V / (_) | | | |".center(shutil.get_terminal_size().columns))
	print ("   |_|\___/ \__,_|   \_/\_/ \___/|_| |_|".center(shutil.get_terminal_size().columns))
	print ("------------------------------------------".center(shutil.get_terminal_size().columns))
	print (("   Best streak: " + str(bestStreak)).center(shutil.get_terminal_size().columns))
	print (("   Score:       " + str(player['score'])).center(shutil.get_terminal_size().columns))
	print ('\n' + "              Main Menu (M)             ".center(shutil.get_terminal_size().columns))
	print ("                Retry (R)               ".center(shutil.get_terminal_size().columns))
def printLevels():
	print('LEVEL SELECTION'.center(shutil.get_terminal_size().columns))
	for n in levels:
		if(int(levels[n]['unlocked']) == 1):
			if(int(levels[n]['completed']) == 1):
				print('Level ' + n + ':     completed     ' + 'Best Streak:   ' + levels[n]['bestStreak'])
			else:
				print('Level ' + n + ':     unlocked')
		else:
			print('Level ' + n + ':     LOCKED')
def printStats():
	print(('Score: ' + str(player['score']) + '          Health: ' + str(player['health']) + '          Streak: ' + str(streak)).center(shutil.get_terminal_size().columns))
def printWord():
	global highlightLetter, word
	print('\n\n\n\n\n     ', end='')
	for n in range(0,len(word)):
		if n == highlightLetter:
			print(f'{Fore.GREEN}'+ word[n] + f'{Style.RESET_ALL}', end='')
			if(word[n] == '.'):
				print('\n    ', end='')
		else:
			print(word[n], end='')
			if(word[n] == '.'):
				print('\n    ', end='')
def getWord():
	global word, levels, selectedLevel
	word = levels[selectedLevel]['text']
	
def reloadMainMenu():
	global mode
	mode = 99
	deleteScreen()
	printMainMenu()
def reloadPlayScreen():
	global mode, player, highlightLetter, streak, word
	player['health'], player['score'], highlightLetter, streak = 10, 0, 0, 0
	mode = 1
	getWord()
	deleteScreen()
	printStats()
	printWord()
def reloadGameOverScreen():
	global mode
	mode = 2
	deleteScreen()
	printGameOver()
def reloadWinScreen():
	global mode
	mode = 3
	deleteScreen()
	printWin()
def reloadLevelsScreen():
	global mode
	mode = 4
	deleteScreen()
	printLevels()
	
def levelsLoad():
	global levels
	levelsinfo = open('gamesave/levelsinfo.txt','r+')
	levels = {	levelsinfo.readline().split('\n')[0]:{
					'text':levelsinfo.readline().split('\n')[0],
					'completed':(levelsinfo.readline().split('\n')[0]),
					'unlocked':(levelsinfo.readline().split('\n')[0]),
					'bestStreak':(levelsinfo.readline().split('\n')[0])
					},
				levelsinfo.readline().split('\n')[0]:{
					'text':levelsinfo.readline().split('\n')[0],
					'completed':(levelsinfo.readline().split('\n')[0]),
					'unlocked':(levelsinfo.readline().split('\n')[0]),
					'bestStreak':(levelsinfo.readline().split('\n')[0])
					},
				levelsinfo.readline().split('\n')[0]:{
					'text':levelsinfo.readline().split('\n')[0],
					'completed':(levelsinfo.readline().split('\n')[0]),
					'unlocked':(levelsinfo.readline().split('\n')[0]),
					'bestStreak':(levelsinfo.readline().split('\n')[0])
					},
				levelsinfo.readline().split('\n')[0]:{
					'text':levelsinfo.readline().split('\n')[0],
					'completed':(levelsinfo.readline().split('\n')[0]),
					'unlocked':(levelsinfo.readline().split('\n')[0]),
					'bestStreak':(levelsinfo.readline().split('\n')[0])
					},
				levelsinfo.readline().split('\n')[0]:{
					'text':levelsinfo.readline().split('\n')[0],
					'completed':(levelsinfo.readline().split('\n')[0]),
					'unlocked':(levelsinfo.readline().split('\n')[0]),
					'bestStreak':(levelsinfo.readline().split('\n')[0])
					},
				levelsinfo.readline().split('\n')[0]:{
					'text':levelsinfo.readline().split('\n')[0],
					'completed':(levelsinfo.readline().split('\n')[0]),
					'unlocked':(levelsinfo.readline().split('\n')[0]),
					'bestStreak':(levelsinfo.readline().split('\n')[0])
					}
			}
	levelsinfo.close()
def levelsSave():
	global levels
	levelsinfo = open('gamesave/levelsinfo.txt','w')
	for n in levels:
		levelsinfo.write(n + '\n')
		levelsinfo.write(levels[n]['text'] + '\n')
		levelsinfo.write(levels[n]['completed'] + '\n')
		levelsinfo.write(levels[n]['unlocked'] + '\n')
		levelsinfo.write(levels[n]['bestStreak'] + '\n')
	levelsinfo.close()
	
	
def runGame():
	global highlightLetter, streak, bestStreak, mode
	global word, selectedLevel
	global levels
	global player
	
	player = {'score': 0, 'health': 10}
	highlightLetter = 0
	streak = 0
	bestStreak = 0
	selectedLevel = '1'
	
	word = ''
	
	levelsLoad()
	
	mode = 99
	
	colorama.init()
	reloadMainMenu()
	
	while(1):
		if(mode == 1):
			try:
				key = getch()
				keyDecoded = key.decode(encoding="utf-8", errors="strict")
				
				if(player['health'] <= 1):
					reloadGameOverScreen()
					bestStreak = 0
				
				elif(keyDecoded == '\x1b'):
					reloadMainMenu()
					
				elif(keyDecoded == word[highlightLetter]):
					highlightLetter = highlightLetter + 1
					streak = streak + 1
					player['score'] = player['score'] + 1 + streak
					
					if(bestStreak < streak):
						bestStreak = streak
					else:
						pass
					
					if(highlightLetter == len(word)):
						levels[selectedLevel]['completed'] = '1'
						
						try:
							levels[str(int(selectedLevel)+1)]['unlocked'] = '1'
						except KeyError:
							pass
							
						if(int(levels[selectedLevel]['bestStreak']) < bestStreak):
							levels[selectedLevel]['bestStreak'] = str(bestStreak)
						
						levelsSave()
						reloadWinScreen()
						bestStreak = 0
						
					else:
						deleteScreen()
						printStats()
						printWord()
						
				elif(keyDecoded != word):
					streak = 0
					player['health'] = player['health'] - 1
					deleteScreen()
					printStats()
					printWord()
				else:
					pass
					
			except UnicodeDecodeError:
				pass
				
		if(mode == 2):
			try:
				key = getch()
				keyDecoded = key.decode(encoding="utf-8", errors="strict")
				
				if(keyDecoded == 'm'):
					reloadMainMenu()
					
				elif(keyDecoded == 'r'):
					reloadPlayScreen()
				else:
					pass
					
			except UnicodeDecodeError:
				pass
				
		if(mode == 3):
			try:
				key = getch()
				keyDecoded = key.decode(encoding="utf-8", errors="strict")
				
				if(keyDecoded == 'm'):
					reloadMainMenu()
					
				elif(keyDecoded == 'r'):
					reloadPlayScreen()
					
				elif(keyDecoded == 'n'):
					pass
					
				else:
					pass
					
			except UnicodeDecodeError:
				pass
		
		if(mode == 4):
				selectedLevel = input('\n\n\n\nYou want to play level:   ')
				if(selectedLevel in levels):
					if(int(levels[selectedLevel]['unlocked']) == 1):
						reloadPlayScreen()
					else:
						reloadLevelsScreen()
				else:
					reloadLevelsScreen()
		
		if(mode == 99):
			try:
				key = getch()
				keyDecoded = key.decode(encoding="utf-8", errors="strict")
				
				if(keyDecoded == 's'):
					reloadPlayScreen()
					
				elif(keyDecoded == 'e'):
					sys.exit(0)
					
				elif(keyDecoded == 'l'):
					reloadLevelsScreen()
				else:
					pass
					
			except UnicodeDecodeError:
				pass

		

runGame()