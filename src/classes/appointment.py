class Appointment:

	def __init__(self, name=None, start=None, end=None):
		""" initialized with a name, the time it starts, and the time it
			finishes
		"""
		self.id = name.capitalize()
		self.start = start
		self.end = end

	def __str__(self):
		""" printed out all the data it is initialized with
		"""
		return self.id, "from", self.start, "until", self.end
