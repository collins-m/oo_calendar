from classes.appointment import Appointment
from classes.day import Day
from classes.week import Week

class Main:

    def __init__(self):
        pass

    def help(self):
        """ prints the user manual
            """
        print("-"*76)
    	print("Add an appointment:")
    	print("add <day> <name of appointment> start-time <hh:mm> finish-time <hh:mm> -24hr")
    	print("-"*76)
    	print("Remove an appointment:")
    	print("remove <day> <name of appointment>")
    	print("-"*76)
    	print("View appointments for whole week:")
    	print("view week")
    	print("-"*76)
    	print("View appointments for given day:")
    	print("view <day>")
    	print("-"*76)
    	print("To exit program:")
    	print("exit")
    	print("-"*76)

    def view_day(self, day):
        """ view a given day and its appointments
            """
        return str(day)

    def view_week(self):
        """ view every day and their appointments
            """
        return str(week)

    def view(self, arg):
        """ this redirects to the appropriate view function
            """
        if arg == "week":
            view_week()
        else:
            view_day(arg) # needs error handling

    def add(self, day, app, start, end):
        """ adds an appointment to the given day
            """
        day.add_appointment(app, start, end)

    def remove(self, app):
        """ removes an appointment from the given day
            """
        day.remove_appointment(app)

    def main():
        """ Runs the program and initializes the environment
            """
        pass

if __name__ == "__main__":
    main = Main()
    Main.main()
