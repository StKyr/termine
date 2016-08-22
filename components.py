#!/usr/bin/python

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#    components.py: source code of termine minesweeper game                   #
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

class cell():
	def __init__(self, contex):
		self.setContex(contex)
	
	def setContex(self, contex):
		if contex==0:
			self.mine=False
			self.empty=True
			self.value=0
		elif contex==-1:
			self.mine=True
			self.empty=False
			self.value=-1
		elif contex>=1 and contex <=8:
			self.mine=False
			self.empty=False
			self.value=contex
		else:
			return
		self.open=False
		self.flag=False
		return
		
	def isMine(self):
		return self.mine
		
	def isEmpty(self):
		return self.empty
		
	def isNum(self):
		return not(self.mine or self.empty)
	
	def isOpen(self):
		return self.open
		
	def hasFlag(self):
		return self.flag
		
	def openCell(self):
		self.open=True
		
	def flagCell(self):
		self.flag=True

	def unflagCell(self):
		self.flag=False
		
	def getNum(self):
		return self.value
		
	def setMine(self):
		self.setContex(-1)
		
		
		
class board():
	def __init__(self, Height, Width, n_mines):
		self.table=[] 
		self.height=Height
		self.width=Width
		self.mines=n_mines
		for i in xrange(self.height):
			self.table.append([])
			for j in xrange(self.width):
				tempcell=cell(0)
				self.table[i].append(tempcell)
				
		self.placeMines()
		self.setNumbers()
		
		return
		
	def getSize(self):
		return str(self.height)+"x"+str(self.width)

	def placeMines(self):

		from random import randint
		placed=0
		while placed<self.mines:
			x=randint(0,self.height-1)
			y=randint(0,self.width-1)
			while self.table[x][y].isMine()==True:
				x=randint(0,self.height-1)
				y=randint(0, self.width-1)
			self.table[x][y].setMine()
			placed+=1
		return
		
	def inBounds(self, x,y):
		if x==self.height or y==self.width:
			return False
		return x>=0 and x<self.height and y>=0 and y<self.width				

	def setNumbers(self):
					
		for row in xrange(self.height):
			for col in xrange(self.width):
				if self.table[row][col].isEmpty()==True:
					adjmines=0
				 	for i in [-1,0,1]:
				 		for j in [-1,0,1]:
				 			if self.inBounds(row+i, col+j)==True:
				 				if self.table[row+i][col+j].isMine()==True:
				 					adjmines+=1
				 	self.table[row][col].setContex(adjmines)
		return
		
	def printBoard(self):
		def clearscreen():
			#print "\n"*50
			return
		
		emptySymbol=" "
		mineSymbol="*"
		closedSymbol="."
		flagSymbol="P"
	
		clearscreen()
		def digits(x):
			dig=1
			while x/10 > 0:
				x=x/10
				dig+=1
			return dig
		spacesLeft=digits(self.height) - 1
		colNumbering="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
		
		linestr=' '*(spacesLeft+1+2)
		for i in xrange(self.width):
			linestr+=colNumbering[i]+" "		
		print linestr
		
		linestr=' '*(spacesLeft+1)+"+ "+("- "*(self.width+2-2))+"+"
		print linestr
		
		for row in xrange(self.height):
			linestr=' '*(spacesLeft-row/9)+str(row+1)+"| "
			for col in xrange(self.width):
				if self.table[row][col].hasFlag()==True:
					linestr+=flagSymbol
				elif self.table[row][col].isOpen()==False:
					linestr+=closedSymbol
				elif self.table[row][col].isEmpty()==True:
					linestr+=emptySymbol
				elif self.table[row][col].isNum()==True:
					linestr+=str(self.table[row][col].getNum())
				elif self.table[row][col].isMine()==True:
					linestr+=mineSymbol
					
				linestr+=" "
			linestr+="~"
			linestr=linestr.replace("~", "|")	# quick way to strip last character
			linestr+=str(row+1)
			print linestr
		
		linestr=' '*(spacesLeft+1)+"+ "+("- "*(self.width+2-2))+"+"
		print linestr
		linestr=' '*(spacesLeft+1+2)
		for i in xrange(self.width):
			linestr+=colNumbering[i]+" "		
		print linestr		
		
		return
		
		
	def openEmpties(self, x, y):

		def openempties(aboard, x, y):
			if aboard.inBounds(x,y)==False: return
			if aboard.table[x][y].isOpen()==True: return
			if aboard.table[x][y].hasFlag()==True: return
			
			if aboard.table[x][y].isNum()==True:
				aboard.table[x][y].openCell()
				return
			
			if aboard.table[x][y].isEmpty()==True:
				aboard.table[x][y].openCell()	
				for i in [-1,0,1]:
					for j in [-1,0,1]:
						if aboard.inBounds(x+i,y+j)==True:
							openempties(aboard, x+i, y+j)
			return

		openempties(self, x, y)
		return

	def play(self, x,y, flag="no flag"):
		if self.inBounds(x,y)==False:
			return -1
			
		if self.table[x][y].isOpen()==True:
			return -3

		if flag=="flag":
			if self.table[x][y].hasFlag()==True:
				self.table[x][y].unflagCell()
				return 10
			else:
				self.table[x][y].flagCell()
				return 20
		elif flag=="no flag":
			pass
		else:
			return -2
				
		if self.table[x][y].isEmpty()==True:
			self.openEmpties(x,y)
			return 0
			
		if self.table[x][y].hasFlag()==True:
			return -4

		if self.table[x][y].isNum()==True:
			self.table[x][y].openCell()
			return 0
		
		if self.table[x][y].isMine()==True:
			return 1
		

		
	def openAll(self):
		for row in xrange(self.height):
			for col in xrange(self.width):
				self.table[row][col].openCell()
		return
		
	def getNumOfClosed(self):
		n=0
		for row in xrange(self.height):
			for col in xrange(self.width):
				if self.table[row][col].isOpen()==False:
					n+=1
		return n

