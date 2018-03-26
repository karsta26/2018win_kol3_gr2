import random
from Plane import Plane

class Environment(object):
	def turbulence(self, plane):
		plane.angle = plane.angle - random.randint(1, 10)