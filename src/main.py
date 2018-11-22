from classes.appointment import Appointment
from classes.day import Day
from classes.week import Week

class Main:

    def __init__(self):
        pass

    def help(self):
        """ prints the user manual
            """
        pass

    def view_day(self, day):
        """ view a given day and its appointments
            """
        pass

    def view_week(self):
        """ view every day and their appointments
            """
        pass

    def view(self, arg):
        """ this redirects to the appropriate view function
            """
        pass

    def add(self, day, app, start, end):
        """ adds an appointment to the given day
            """
        pass

    def remove(self, app):
        """ removes an appointment from the given day
            """
        pass

    def main():
        """ Runs the program and initializes the environment
            """
        pass

if __name__ == "__main__":
    main = Main()
    Main.main()
