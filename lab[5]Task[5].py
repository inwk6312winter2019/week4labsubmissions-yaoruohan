class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def __str__(self):
		return "The Points are ({},{})".format(self.x,self.y)

	def add(self,other):
		print (self.x+other.x,self.y+other.y)


o1=Point(25,35)
o2=Point(30,40)
print(o1)
print(o2)
o1.add(o2)




