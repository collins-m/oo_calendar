from appointment import Appointment

class Day:

	def __init__(self, name):
		""" Initialized with a name, and a list of appointments.
		"""
		self.id = name
		self.appointments = []

	def add_appointment(self, name, start, end):
		""" Using the Appointment class, we append an Appointment object
			to the list.
		"""
		name = Appointment(name, start, end)
		self.appointments.append(name)

	def remove_appointment(self, name):
		""" We remove the selected Appointment from the object.
		"""
		pass

	def __str__(self):
		""" Prints the Day, and its list of Appointments.
		"""
		pass
