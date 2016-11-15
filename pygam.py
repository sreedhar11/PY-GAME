import os
import random

class players() :
	def inti(self) :
		self.pnum = input("Enter the no of heroes :")
        self.enum = pnum
		i=0
		self.name = [[]]
		self.role = [[]]
		self.ptp=0
        self.etp
		self.lyf = [[]]
		self.isalive = [[]]
		self.ab = [[]]
		self.row = [[]]
		self.col = [[]]
		x = " "


		while i!=self.pnum :
            choice = input("PLAYER (P) OR ENEMY (E) ? ")
            if choice == 'P' :
                self.pname.append(input("Enter a 5 letter name for PLAYER "))
			    y = input("Ener the role ")
			    self.role.append(y)
			    if self.role[i]==1 :
				    self.plyf.append(300)
				    self.ab.append([2,2,2,2])
				    self.isalive.append(True)
			    elif self.role[i]==2 :
				    self.plyf.append(100)
				    self.ab.append([1,1,1,1])
				    self.isalive.append(True)
                    self.ptp=0
			        i = i+1
