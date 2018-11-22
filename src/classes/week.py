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
            "sun": [],
        	"mon": [],
        	"tue": [],
        	"wed": [],
        	"thu": [],
        	"fri": [],
        	"sat": [],

        }

    def __str__(self):
        """ prints each of the days in turn
            """
        apps = []
        for day in self.days:
            apps.append(str(day))
        apps = "\n".join(apps)
        return apps
