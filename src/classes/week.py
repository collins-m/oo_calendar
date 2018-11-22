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

    def __str__(self):
        """ prints each of the days in turn
        """
        apps = []
        for day in self.a_days:
            apps.append(str(self.days[day]))
        apps = "\n".join(apps)
        return apps
