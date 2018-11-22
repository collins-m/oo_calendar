from classes.appointment import Appointment
from classes.day import Day
from classes.week import Week

class Main:

    def __init__(self):
        self.week = Week()

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
        print(str(self.week.days[day]))

    def view_week(self):
        """ view every day and their appointments
        """
        print(str(self.week))

    def view(self, arg):
        """ this redirects to the appropriate view function
        """
        if arg == "week":
            self.view_week()
        else:
            self.view_day(arg)

    def add(self, command):
        """ adds an appointment to the given day
        """
        day, app, start, end = command[0], command[1], command[2], command[3]
        self.week.days[day].add_appointment(app, start, end)

    def remove(self, command):
        """ removes an appointment from the given day
        """
        day, app = command[0], command[1]
        week.days[day].remove_appointment(app)

    def main(self):
        """ Runs the program and initializes the environment
        """
        print("Welcome to OO Calendar in python.")
        print("Type \"help\" for a list of commands.")
        print("-"*76)
        while 1:
            # try:
            command = input().split()
            print()

            if command[0] == "exit":
                print("Goodbye.")
                break

            elif command[0] == "help":
                self.help()

            elif command[0] == "view":
                self.view(command[1])

            elif command[0] == "add":
                self.add(command[1:])

            elif command[0] == "remove":
                self.remove(command[1:])

            # except:
                # print("Input Error, type \"help\" for a list of commands")

if __name__ == "__main__":
    main = Main()
    main.main()
