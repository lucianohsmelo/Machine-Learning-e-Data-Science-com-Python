class Robo2D(object):
	"""docstring for ClassName"""
	def __init__(self, x,y):
		self.x = x
		self.y = y

	def print_x(self):
		print(self.x)


class Robo3D(Robo2D):
	"""docstring for ClassName"""
	def __init__(self, x, y, z):
		super(Robo3D, self).__init__(x, y)
		self.z = z
		

robo1 = Robo2D(1,2)
robo1.print_x()

robo2 = Robo3D(5,2,3)
robo2.print_x()


		
		