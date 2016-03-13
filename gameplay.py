#!/usr/bin/python

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#    gameplay.py: source code of termine minesweeper game                     #
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

from components import board

class game:

	numOfMines=0
	dimHeight=0
	dimWidth=0
	remMines=0
	numOfFlags=0

	def setNew(self, height, width, n_mines):
		if width<=0 or height<=0 or n_mines<=0:
			return False
		if width>2*26 or height>2*26 or n_mines > width*height:
			return False

		self.numOfMines=n_mines
		self.dimHeight=height
		self.dimWidth=width
		self.remMines=self.numOfMines
		self.numOfFlags=0
		
		self.playBoard=board(self.dimHeight, self.dimWidth, self.numOfMines)
		
		return True
		
	def gameWon(self):
		if self.playBoard.getNumOfClosed()==self.numOfMines: return True
		return False
		
		
	def playMove(self, x,y,flag):
			
		if flag=="no flag":
			res=self.playBoard.play(x,y)
		elif flag=="flag":
			res=self.playBoard.play(x,y, "flag")
		else:
			res=-2
		
		if res==-4:
			print "Cannot open a cell with a flag."		
		elif res==-3:
			print "This cell is already open."
		elif res==-1:
			print "Invalid row/column coordinates."
		elif res==1:
			return -1
		elif res==0:
			pass
		elif res==10:
			self.numOfFlags-=1
		elif res==20:
			self.numOfFlags+=1
		elif res==-2:
			print "Invalid internal command."
			
		if self.gameWon()==True: return 1
		return 0
		
	def printBoard(self):
		self.playBoard.printBoard()

	def showOpenBoard(self):
		self.playBoard.openAll()
		self.playBoard.printBoard()
		
	def getCommand(self):
		row,col,flag = None, None, None
		h, w, m = None, None, None
		
		com=raw_input("Type command: ")
		args=com.split(" ")

		if args==[""]:
			print "No command inserted"
			return self.getCommand()
			
		if args[0]=="newgame" or args[0]=="newgame".upper():
		
			if len(args)==1:
				pass
				return -1, row, col, flag, h, w, m
				
			if len(args)==3:
				try:
					h=int(args[1])
					w=h
				except:
					print "Invalid size"
					return -1, row, col, flag, h, w, m
					
				try:
					m=int(args[2])
				except:
					print "Invalid number of mines"
					return -1, row, col, flag, h, w, m
					
				return 11, row, col, flag, h, w, m
				
			if len(args)==4:
				try:
					h=int(args[1])
				except:
					print "Invalid number of rows"
					return -1, row, col, flag, h, w, m
					
				try:
					w=int(args[2])
				except:
					print "Invalid number of columns"
					return -1, row, col, flag, h, w, m
					
				try:
					m=int(args[3])
				except:
					print "Invalid number of mines"
					return -1, row, col, flag, h, w, m
					
				return 11, row, col, flag, h, w, m
			
			print "Unknown structure of command 'newgame'"
			return -1, row, col, flag, h, w, m
			
		if args[0]=="endgame" or args[0]=="endgame".upper():
			return 20, row, col, flag, h, w, m

		if args[0]=="quit" or args[0]=="quit".upper():
			return 40, row, col, flag, h, w, m

		if args[0]=="showcommands" or args[0]=="showcommands".upper():
			return 30, row, col, flag, h, w, m
			
		if args[0]=="open" or args[0]=="open".upper():
			flag="no flag"
			if len(args)!=2:
				print "Unknown structure of command 'open'"
				return -1, row, col, flag, h, w, m
				
			COLS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
			col_letter = args[1][0]
			col=COLS.find(col_letter)
			if col==-1:
				print "Invalid column coordinate"
				return -1, row, col, flag, h, w, m
				
			try:
				row=int(args[1][1:])
				row-=1
			except:
				print "Invalid row coordinate"
				return -1, row, col, flag, h, w, m
		
			return 0, row, col, flag, h, w, m
			
		if args[0]=="flag" or args[0]=="flag".upper() or args[0]=="f" or args[0]=="f".upper():
			flag="flag"
			if len(args)!=2:
				if args[0]=="flag" or args[0]=="flag".upper():
					print "Unknown structure of command 'flag'"
				else:
					print "Unknown structure of command 'f'"
				return -1, row, col, flag, h, w, m
				
			COLS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
			col_letter = args[1][0]
			col=COLS.find(col_letter)
			if col==-1:
				print "Invalid column coordinate"
				return -1, row, col, flag, h, w, m
				
			try:
				row=int(args[1][1:])
				row-=1
			except:
				print "Invalid row coordinate"
				return -1, row, col, flag, h, w, m
		
			return 0, row, col, flag, h, w, m
			
		print "Unknown command"
		return -1, row, col, flag, h, w, m
