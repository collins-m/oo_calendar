class Day:

	def __init__(self, name=None):
		""" initialized with a name, and a list of appointments
			"""
		self.id = name
		self.appointments = []

    def check_overlap(self, element):
        """ check if appointment overlaps with another appointment in the
            given day, returns true if no overlap
            """
        for appointment in self.appointments:
            if ((element.start < appointment.start) and (appointment.start < element.end)) or ((element.start < appointment.end) and (appointment.end < element.end)):
                return False
            else:
                return True

    def take_start_time(self, element):
        """ helper function to return start-time for sorting lists
            """
        return element.start

	def add_appointment(self, name, start, end):
		""" using the appointment class, we append an appointment object
			to the list, it keeps them in chronological order as well
			"""
		name = Appointment(name, start, end)
        if check_overlap(name):
    		self.appointments.append(name)
            self.appointments.sort(key=take_start_time)
        else:
            print("Invalid appointment time, overlaps with another appointment.")

	def remove_appointment(self, name):
		""" removes the selected appointment from the object
			"""
		self.appointments.remove(name)

	def __str__(self):
		""" prints the day, and its list of appointments
			"""
        apps = []
        for app in self.appointments:
            apps.append(str(app))
        apps.append("-"*50)
        apps = "\n".join(apps)
		return "Appointments for", self.name.capitalize()+"\n\n"+apps
