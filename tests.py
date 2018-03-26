# https://github.com/Shpiler7/kol1_gr2
import unittest
from Plane import Plane
from Environment import Environment
import math

class MyTest(unittest.TestCase):

	def setUp(self):
		self.plane_name = "Airbus"
		self.test_instance_of_Plane = Plane(self.plane_name)
		self.test_instance_of_Environment = Environment()


	def test_init_Plane(self):
		self.assertEqual(self.test_instance_of_Plane.name, self.plane_name)

	def test_init_Plane_with_number(self):
		tmp_plane = Plane(1223)
		self.assertEqual(tmp_plane.name, 1223)

	def test_init_Plane_with_trash(self):
		tmp_plane = Plane("../././")
		self.assertEqual(tmp_plane.name, "../././")

	def test_str_in_Plane(self):
		self.assertEqual(str(self.test_instance_of_Plane), self.plane_name)

	def test_str_in_Plane_another_example(self):
		self.assertNotEqual(str(self.test_instance_of_Plane), "")

	def test_str_in_Plane_not_null(self):
		self.assertNotEqual(str(self.test_instance_of_Plane), None)

	def test_tilt_correction_in_Plane(self):
		self.test_instance_of_Plane.tiltCorrection()
		self.assertEqual(self.test_instance_of_Plane.angle, 90)

	def test_turbulance_in_Environment(self):
		self.test_instance_of_Environment.turbulence(self.test_instance_of_Plane)
		self.assertNotEqual(self.test_instance_of_Plane.angle, 90)

	def test_turbulance_in_Environment_another_plane(self):
		tmp_plane = Plane("Air")
		self.test_instance_of_Environment.turbulence(tmp_plane)
		self.assertNotEqual(tmp_plane, 90)

	def test_turbulance_in_another_Environment_another_plane(self):
		tmp_plane = Plane("Air")
		tmp_environment = Environment()
		tmp_environment.turbulence(tmp_plane)
		self.assertNotEqual(tmp_plane, 90)

