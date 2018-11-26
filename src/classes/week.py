from classes.day import Day

class Week:

    def __init__(self):
        """ initialized with a list of day objects
        """
        self.a_days = [
            "sun",
            "mon",
            "tue",
            "wed",
            "thu",
            "fri",
            "sat"
        ]
        self.days =  {
            "sun": Day("sun"),
        	"mon": Day("mon"),
        	"tue": Day("tue"),
        	"wed": Day("wed"),
        	"thu": Day("thu"),
        	"fri": Day("fri"),
        	"sat": Day("sat"),

        }

    def view_day(self, day):
        """ view a given day and its appointments
        """
        print(str(self.days[day]))

    def add(self, command):
        """ adds an appointment to the given day
        """
        day, app, start, end = command[0], command[1], command[2], command[3]
        self.days[day].add_appointment(app, start, end)

    def remove(self, command):
        """ removes an appointment from the given day
        """
        day, app = command[0], command[1]
        self.days[day].remove_appointment(app)

    def __str__(self):
        """ prints each of the days in turn
        """
        apps = []
        for day in self.a_days:
            apps.append(str(self.days[day]))
        apps = "\n".join(apps)
        return "{}".format(apps)
