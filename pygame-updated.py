import os
import random

class env() :
	lout = [["     " for i in range(10)] for j in range(10)]
	leb = 0
	rib = 9
	ub = 0
	lb = 9
	def place(self,o1,o2) :
		p1 = players()
		e1 = enemy()
		p1 = o1
		e1 = o2
		n = p1.pnum
		i=0
		while n!=0 :
			pos = input("Enter the position to place player in first row"+str(i))
			self.lout[0][pos] = p1.pname[i]
			p1.row.append(0)
			p1.col.append(pos)
			ex = random.randrange(1, 8, 1)
			ey = random.randrange(1, 8, 1)
			self.lout[ex][ey] = e1.ename[i]
			e1.row.append(ex)
			e1.col.append(ey)
			n = n-1
			i = i+1

	def check(self,o1,move,di,select) :
		if o1.isalive[select] == True :
			if di == 8 and self.ub < o1.row[select]-move :
				if move > o1.ab[select][2] :
					print "PLAYER CANNOT MOVE THAT DISTANCE"
					return False
				else :
					return True

			elif di == 2 and self.lb > o1.row[select]+move :
				if move > o1.ab[select][3] :
					print "PLAYER CANNOT MOVE THAT DISTANCE"
					return False
				else :
					return True

			elif di == 4 and self.leb < o1.col[select]-move :
				if move > o1.ab[select][0] :
					print "PLAYER CANNOT MOVE THAT DISTANCE"
					return False
				else :
					return True

			elif di == 6 and self.rib > o1.col[select]+move :
				if move > o1.ab[select][1] :
					print "PLAYER CANNOT MOVE THAT DISTANCE"
					return False
				else :
					return True

		else :
			return False

	def movePlayer(self,pi,di,select,e) :
		move = pi.ab[select][0]
		if di == 8 :

			p = pi.row[select]
			if self.ub > pi.row[select]-move :
				x = 0
			else :
				x = pi.row[select]-move
			q = pi.col[select]
			y = pi.col[select]
			r = e.row[select]
			s = e.col[select]
			if x == r and y == s:
				self.lout[x][y] = '     '
				self.lout[p][q] = '     '
				pi.plyf[select] = 0
				e.elyf[select] = 0
				e.isalive = False
				pi.plyf = False
				pi.ptp = pi.ptp + 100
				print "YOU HAVE DONE IT"
				print "TOTAL POINTS FOR PLAYER :",
				print pi.ptp
				os._exit(0)

			else :
				self.lout[p][q] = '     '
				self.lout[x][y] = pi.pname[select]

			pi.row[select] = x
			pi.col[select] = y
			print self.lout[x][y]

		if di == 2 :
			p = pi.row[select]
			q = pi.col[select]
			if self.lb < pi.row[select]+move :
				x = 9
			else :
				x = pi.row[select]+move
			y = pi.col[select]

			r = e.row[select]
			s = e.col[select]
			if x == r and y == s:
				self.lout[x][y] = '     '
				self.lout[p][q] = '     '
				pi.plyf[select] = 0
				e.elyf[select] = 0
				e.isalive = False
				pi.plyf = False
				pi.ptp = pi.ptp + 100
				print "YOU HAVE DONE IT"
				print "TOTAL POINTS FOR PLAYER :",
				print pi.ptp
				os._exit(0)
			else :
				self.lout[p][q] = '     '
				self.lout[x][y] = pi.pname[select]

			pi.row[select] = x
			pi.col[select] = y
			print self.lout[x][y]

		if di == 4 :
			p = pi.row[select]
			q = pi.col[select]
			x = p
			if pi.col[select]-move <= 0 :
				y = 0
			else :
				y = pi.col[select]-move
			r = e.row[select]
			s = e.col[select]
			if x == r and y == s:
				self.lout[x][y] = '     '
				self.lout[p][q] = '     '
				pi.plyf[select] = 0
				e.elyf[select] = 0
				e.isalive = False
				pi.plyf = False
				pi.ptp = pi.ptp + 100
				print "YOU HAVE DONE IT"
				print "TOTAL POINTS FOR PLAYER :",
				print pi.ptp
				os._exit(0)

			else :
				self.lout[p][q] = '     '
				self.lout[x][y] = pi.pname[select]

			pi.row[select] = x
			pi.col[select] = y
			print self.lout[x][y]

		if di == 6 :
			p = pi.row[select]
			q = pi.col[select]
			x = p
			if pi.col[select]+move >= 9 :
				y = 9
			else :
				y = pi.col[select]+move
			r = e.row[select]
			s = e.col[select]
			if x == r and y == s:
				self.lout[x][y] = '     '
				self.lout[p][q] = '     '
				pi.plyf[select] = 0
				e.elyf[select] = 0
				e.isalive = False
				pi.plyf = False
				pi.ptp = pi.ptp + 100
				print "YOU HAVE DONE IT"
				print "TOTAL POINTS FOR PLAYER :",
				print pi.ptp
				os._exit(0)

			else :
				self.lout[p][q] = '     '
				self.lout[x][y] = pi.pname[select]

			pi.row[select] = x
			pi.col[select] = y
			print self.lout[x][y]

	def moveEnemy(self,pi,di,select,e):

		s = select
		t1 = random.randrange(0, 1, 1)
		t2 = random.randrange(0, 1, 1)
		x = e.row[s] + t1
		y = e.col[s] + t2
		p = e.row[s]
		q = e.col[s]
		r = pi.row[s]
		s = pi.col[s]
		if x == r and y == s:
			if pi.plyf[s] > e.elyf[s] :
				self.lout[x][y] = pi.pname[s]
				self.lout[p][q] = '     '
				pi.plyf[s] = pi.plyf[s] - e.elyf[s]
				e.elyf[s] = 0
				e.isalive = False
				pi.ptp = pi.ptp + 100
			elif pi.plyf[s] < e.elyf[s] :
				self.lout[x][y] = e.ename[s]
				self.lout[p][q] = '     '
				e.elyf[s] = e.elyf[s] - pi.plyf[s]
				pi.plyf[s] = 0
				pi.isalive = False
				e.etp = e.etp + 100
			elif pi.plyf[s] == e.elyf[s] :
				self.lout[x][y] = '     '
				self.lout[p][q] = '     '
				pi.plyf[s] = 0
				e.elyf[s] = 0
				e.isalive = False
				pi.plyf = False
				pi.ptp = pi.ptp + 100

		else :
			self.lout[p][q] = '     '
			self.lout[x][y] = e.ename[s]

		e.row[s] = x
		e.col[s] = y






class players() :
	def inti(self) :
		self.pnum = 1
		i=0
		self.pname = []
		self.role = []
		self.ptp=0
		self.plyf = []
		self.isalive = []
		self.ab = []
		self.row = []
		self.col = []
		x = " "


		while i!=self.pnum :

			self.pname.append(input("Enter a 5 letter name (NOTE : SPECIFY IN DOUBLE QUOTES) "))
			y = 1
			self.role.append(y)
			if self.role[i]==1 :
				self.plyf.append(100)
				self.ab.append([2,2,2,2])
				self.isalive.append(True)
			else :
				self.role[i]==2
				self.plyf.append(100)
				self.ab.append([1,1,1,1])
				self.isalive.append(True)
			self.ptp=0
			i = i+1




class enemy() :
	def einti(self,n) :
		pp = players()

		self.en = n
		i=0
		self.ename = []
		self.erole = []
		self.etp=0
		self.elyf = []
		y = 1
		self.isalive = True
		self.ab =[]
		self.row = []
		self.col = []


		while i!=self.en :
			x = "ENE_"+str(i)
			self.ename.append(x)
			self.erole.append(y)
			y = y+1
			if self.erole[i]==1 :
				self.elyf.append(100)
				self.ab.append([2,2,2,2])
			else :
				self.erole[i]==2
				self.elyf.append(100)
				self.ab.append([1,1,1,1])

			self.etp=0
			i = i+1

pi = players()
pi.inti()
print pi.pname
print pi.role
print pi.plyf
print pi.isalive
print pi.ab

e = enemy()
n = pi.pnum
e.einti(n)
print e.ename
print e.erole
print e.elyf
print e.isalive
print e.ab

en = env()
en.place(pi,e)

k = 0
for k in range(0,10) :
	print en.lout[k]
	c = True
while c :
	select = 0
	di = input("Enter the direciton")

	if di==8 :
		en.movePlayer(pi,di,select,e)
		#en.moveEnemy(pi,di,select,e)
		os.system('clear')
		for k in range(0,10) :
			print en.lout[k]
	if di==2 :
		en.movePlayer(pi,di,select,e)
		#en.moveEnemy(pi,di,select,e)
		os.system('clear')
		for k in range(0,10) :
			print en.lout[k]
	if di==4 :
		en.movePlayer(pi,di,select,e)
		#en.moveEnemy(pi,di,select,e)
		os.system('clear')
		for k in range(0,10) :
			print en.lout[k]
	if di==6 :
		en.movePlayer(pi,di,select,e)
		#en.moveEnemy(pi,di,select,e)
		os.system('clear')
		for k in range(0,10) :
			print en.lout[k]
#	o=input("PRESS 0 TO QUIT...ANY OTHER INTEGER TO CONTINUE? ")
#	if o == 0 :

	#	for q in range(0,pi.pnum) :
		#if e.isalive[0] == True :
		#		o=1

		#if o != 1 :
		#	c = False




k = 0
for k in range(0,10) :
	print en.lout[k]
print "TOTAL POINTS FOR PLAYER :",
print pi.ptp
