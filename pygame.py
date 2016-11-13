class players() :
	def inti(self) :
		n = input("Enter the no of heros :")
		i=0
		self.pname = []
		self.role = []
		self.ptp=0
		self.plyf = []


		while i!=n :
			x = (input("Enter the name"))
			self.pname.append(x)
			y = input("Ener the role")
			self.role.append(y)
			if self.role[i]==1 :
				self.plyf.append(300)
			elif self.role[i]==2 :
				self.plyf.append(200)
			elif self.role[i]==3 :
				self.plyf.append(150)
			else :
				self.plyf.append(100)
			self.ptp=0
			i = i+1

class enemy() :
	def einti() :
		ename = input("\"Enter the name\"")
		erole = input("Ener the role")
		if erole==1 :
			elyf = 300
		elif erole==2 :
			elyf = 200
		elif erole==3 :
			elyf=150
		else :
			elyf=100
		etp=0

pi = players()
pi.inti()
print pi.pname
print pi.role
print pi.plyf
