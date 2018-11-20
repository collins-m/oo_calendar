class Appointment:

	def __init__(self, name=None, start=None, end=None):
		""" Initialized with a name, the time it starts, and the time it finishes.
		"""
		self.id = name
		self.start = start
		self.end = end

	def __str__(self):
		""" Printed out all the data it is initialized with.
		"""
		pass
