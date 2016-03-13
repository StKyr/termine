#!/usr/bin/python

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#    termine.py: source code of termine minesweeper game                      #
#    Copyright (C) 2016 Stylianopoulos Kyriakos                               #
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from gameplay import game
import sys
	
paramList=["--help", "--dimension", "-d", "--color", "-c", "--width", "-w", "--height", "-h", "--mines", "-m", "--live", "-l", "--commands"]

height, width, mines= None, None, None

commandsList="""
	COMMANDS:
	open [column-letter][row-number]	open cell with corresponding coordinates(no spaces between them).
	flag [column-letter][row-number]	if corresponding cell has no flag, set a flag there, else, remove the flag
	newgame					start a new game ( if there is a game active, that game ends )
	newgame [dimension] [mines-number]	start a new game in a [dimension]x[dimension] board with [mines-number] mines
	newgame [height] [width] [mines-number]	start a new game in a [height]x[width] board with [mines-number] mines
	endgame					if there is an active game, end current game
	quit					exit program
	showcommands				print commands help page
	
	Column letters are case sensitive, commands are not.
	"""
def printHelpPage():
	print """
Usage: termine [OPTION]...

	ARGUMENTS:
	--help			print this help page and exit
	-d, --dimension [n] 	start a game in a [n]x[n] board
	-w, --width [w]		start a game in a board with [w] columns
	-h, --height [h]	start a game in a board with [h] rows
	-m, --mines [m]		start a game in a board with [m] mines
	--comands		print command names list and exit
"""
	print commandsList

def arguments(argv=None):
	if argv is None:
		argv = sys.argv

	first=True
	for arg in argv:
		if first==True:
			first=False
			continue
		if arg in paramList:
			continue
		else:
			try:
				x=int(arg)
			except:
				print "Error: Unrecognized argument '"+arg+"'. Type --help for instructions."
				sys.exit(1)
	
	if "--help" in argv:
		printHelpPage()
		sys.exit(0)

	if "--dimension" in argv or "-d" in argv:
		if "--mines" in argv or "-m" in argv:
			try:
				argPlace=argv.index("--dimension")
			except:
				argPlace=argv.index("-d")
				
			if argPlace<len(argv)-1:
				try:
					height=int(argv[argPlace+1])
					width=height
				except:
					print "Error: Invalid dimension number."
					sys.exit(1)
			else:
				print "Error: No dimension number found."
				sys.exit(1)
				
			try:
				argPlace=argv.index("--mines")
			except:
				argPlace=argv.index("-m")
			
			if argPlace<len(argv)-1:	 
				try:
					mines=int(argv[argPlace+1])
				except:
					print "Error: Invalid number of mines."
					sys.exit(0)
			else:
				print "Error: No number of mines found found."
				sys.exit(0)
				
			
		else:
			print "Error: Also expected -m or --mines argument."
			sys.exit(1)

		if currgame.setNew(height, width, mines)==False:
			print "Error: Invalid board specifications."
			sys.exit(1)
		currgame.printBoard()
		return True
	
	if ("--with" in argv or "-w" in argv) and ("--height" in argv or "-h" in argv) and ("--mines" in argv or "-m" in argv):
		try:
			argPlace=argv.index("--height")
		except:
			argPlace=argv.index("-h")
		
		if argPlace>=len(argv)-1:
			print "Error: No number of rows found."
			sys.exit(0)
		else:
			try:
				height=int(argv[argPlace+1])
			except:
				print "Error: Invalid number of rows."
				sys.exit(0)
		
		try:
			argPlace=argv.index("--width")
		except:
			argPlace=argv.index("-w")
		
		if argPlace>=len(argv)-1:
			print "Error: No number of columns found."
			sys.exit(0)
		else:
			try:
				width=int(argv[argPlace+1])
			except:
				print "Error: Invalid number of columns."
				sys.exit(0)
				
		try:
			argPlace=argv.index("--mines")
		except:
			argPlace=argv.index("-m")
			
		if argPlace<len(argv)-1:	 
			try:
				mines=int(argv[argPlace+1])
			except:
				print "Error: Invalid number of mines."
				sys.exit(0)
		else:
			print "Error: No number of mines found found."
			sys.exit(0)
	
		if currgame.setNew(height, width, mines)==False:
			print "Error: Invalid board specifications."
			sys.exit(1)
		currgame.printBoard()
		return True
	
	if "--commands" in argv:
		print commandsList
		
	if "-m" in argv or "--mines" in argv:
		if ("-w" in argv or "--width" in argv) and ("-h" in argv or "--height" in argv):
			pass
		else:
			if "-d" in argv or "--dimension" in argv:
				pass
			else:
				print "Invalid arguments."
				sys.exit(1)	

	return False
	
def main(currgame):

	nowPlaying=arguments()
	commandCode=0
	row, col, flag = None, None, None
	while commandCode!=40:
		commandCode, row, col, flag, height, width, mines = currgame.getCommand()
	
		if commandCode==0:
			if nowPlaying==True:
				res=currgame.playMove(row, col, flag)
				if res==0:
					currgame.printBoard()
					continue
				if res==-1:
					print "You Lost..."
					currgame.showOpenBoard()
					continue
				if res==1:
					print "You Won!"
					currgame.showOpenBoard()
					continue
			else:
				print "No games started yet."
				continue
	
		if commandCode==11:
			newgame=game()
			currgame=newgame
			if currgame.setNew(height, width, mines)==False:
				print "Invalid board specifications"
				nowPlaying=False
				continue
			currgame.printBoard()
			nowPlaying=True
		
		if commandCode==20:
			nowPlaying=False
			
		if commandCode==30:
			print commandsList
			
		if commandCode==-1:
			continue	

	return 0


currgame=game()
main(currgame)
sys.exit(0)
