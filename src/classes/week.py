class Week:

    def __init__(self, days=None):
        """ initialized with a list of day objects
            """
        self.days =  days

    def __str__(self):
        """ prints each of the days in turn
            """
        apps = []
        for day in self.days:
            apps.append(str(day))
        apps = "\n".join(apps)
        return apps
