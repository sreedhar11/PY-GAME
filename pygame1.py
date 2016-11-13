class env() :
	lout = [[0 for i in range(10)] for j in range(10)]
	leb = 0
	rib = 10
	ub = 0
	lb = 10
	def place(self,o1,o2) :
		p1 = players()
		e1 = enemy()
		p1 = o1
		e1 = o2
		n = p1.pnum
		i=0
		while n!=0 :
			pos = input("Enter the position to place player "+str(i))
			self.lout[0][pos] = p1.pname[i]
			p1.row.append(0)
			p1.col.append(pos)
			self.lout[9][pos] = e1.ename[i]
			n = n-1
			i = i+1

	def check(self,o1,move,di,select) :
		if o1.isalive[select] == True :
			if di == 8 and self.ub <= o1.row[select]-move :
				return True

			elif di == 2 and self.lb >= o1.row[select]+move :
				print o1.row[select]+move
				return True

			elif di == 4 and self.leb <= o1.col[select]-move :
				return True

			elif di == 6 and self.rib >= o1.col[select]+move :
				return True

		else :
			return False

	def movePlayer(self,pi,move,di,select) :
		if di == 8 :
			p = pi.row[select]
			q = pi.col[select]
			x = pi.row[select]-move
			y = pi.col[select]
			self.lout[x][y] = pi.pname[select]
			self.lout[p][q] = 0
			pi.row[select] = x
			pi.col[select] = y
			print self.lout[x][y]

		if di == 2 :
			p = pi.row[select]
			q = pi.col[select]
			print p
			print q
			x = pi.row[select]+move
			y = pi.col[select]
			self.lout[x][y] = pi.pname[select]
			self.lout[p][q] = 0
			pi.row[select] = x
			pi.col[select] = y
			print self.lout[x][y]

		if di == 4 :
			p = pi.row[select]
			q = pi.col[select]
			x = pi.row[select]
			y = pi.col[select]-move
			self.lout[x][y] = pi.pname[select]
			self.lout[p][q] = 0
			pi.row[select] = x
			pi.col[select] = y
			print self.lout[x][y]

		if di == 6 :
			p = pi.row[select]
			q = pi.col[select]
			x = pi.row[select]
			y = pi.col[select]+move
			self.lout[x][y] = pi.pname[select]
			self.lout[p][q] = 0
			pi.row[select] = x
			pi.col[select] = y
			print self.lout[x][y]







class players() :
	def inti(self) :
		self.pnum = input("Enter the no of heros :")
		i=0
		self.pname = []
		self.role = []
		self.ptp=0
		self.plyf = []
		self.isalive = []
		self.ab = []
		self.row = []
		self.col = []


		while i!=self.pnum :
			x = (input("Enter the name"))
			self.pname.append(x)
			y = input("Ener the role")
			self.role.append(y)
			if self.role[i]==1 :
				self.plyf.append(300)
				self.ab.append([4,4,4,4])
				self.isalive.append(True)
			elif self.role[i]==2 :
				self.plyf.append(200)
				self.ab.append([3,3,3,3])
				self.isalive.append(True)
			elif self.role[i]==3 :
				self.plyf.append(150)
				self.ab.append([2,2,2,2])
				self.isalive.append(True)
			else :
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


		while i!=self.en :
			x = "ENEMY_"+str(i)
			self.ename.append(x)
			self.erole.append(y)
			y = y+1
			if self.erole[i]==1 :
				self.elyf.append(300)
				self.ab.append([4,4,4,4])
			elif self.erole[i]==2 :
				self.elyf.append(200)
				self.ab.append([3,3,3,3])
			elif self.erole[i]==3 :
				self.elyf.append(150)
				self.ab.append([2,2,2,2])
			else :
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
print en.lout
q=1
while q!=5 :
	select = input("Select the player")
	di = input("Enter the direciton")
	move = input("Enter the ip")
	if di==8 :
		ret = en.check(pi,move,di,select)
		if ret == True :
			en.movePlayer(pi,move,di,select)
		else :
			print "INVALID MOVE"

	if di==2 :
		ret = en.check(pi,move,di,select)
		if ret == True :
			en.movePlayer(pi,move,di,select)
		else :
			print "INVALID MOVE"

	if di==4 :
		ret = en.check(pi,move,di,select)
		if ret == True :
			en.movePlayer(pi,move,di,select)
		else :
			print "INVALID MOVE"

	if di==6 :
		ret = en.check(pi,move,di,select)
		if ret == True :
			en.movePlayer(pi,move,di,select)
		else :
			print "INVALID MOVE"
	q = q+1


print en.lout
