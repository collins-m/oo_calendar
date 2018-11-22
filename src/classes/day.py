from classes.appointment import Appointment

class Day:

    def __init__(self, name=None):
        """ initialized with a name, and a list of appointments
            """
        self.id = name
        self.appointments = []

    def min_conv(time):
        """ converts time <hh:mm> to minute integer
        """
        hh, mm = time.split(":")
        minutes = (hh * 60) + mm
        return minutes

    def no_overlap(self, start, end):
        """ check if appointment overlaps with another appointment in the
            given day, returns true if no overlap
        """
        for appointment in self.appointments:

            if ((self.min_conv(start) <self. min_conv(appointment.start)) and (self.min_conv(appointment).start < self.min_conv(end))) or ((self.min_conv(start) <self. min_conv(appointment).end) and (self.min_conv(appointment).end < self.min_conv(end))):
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
        if self.no_overlap(start, end):
            name = Appointment(name, start, end)
            self.appointments.append(name)
            self.appointments.sort(key=self.take_start_time)
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
        apps.append("-"*76)
        apps = "\n".join(apps)
        return "Appointments for", self.id.capitalize()+"\n\n"+apps
