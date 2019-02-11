class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def __str__(self):
		return "The Points are ({},{})".format(self.x,self.y)

	def __add__(self,ob):
		print (self.x+ob.x,self.y+ob.y)
	def add(self,ob):
		if isinstance(ob,tuple):
                     print(self.x+ob[0],self.y+ob[1])
		else:
			print(self+ob)

o1=Point(25,35)
o2=Point(35,45)
print(o1)
print(o2)
o1.add(o2)
o1.add((25,35)




