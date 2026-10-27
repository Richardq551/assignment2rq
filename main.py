"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semster_cost = float(annual_cost) / SEMESTERS_PER_YEAR
    return semster_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    monthly_cost = float(annual_cost) / MONTHS_PER_YEAR
    return monthly_cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    daily_cost = float(annual_cost) / (CLASS_DAYS_PER_SEMESTER*2)
    return daily_cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    cost_semester= cost_per_semester(annual_cost)
    credit_cost= float(cost_semester) / float(credits)
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    cost_credit = cost_per_credit(annual_cost, credits)
    class_cost = float(cost_credit) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return class_cost


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = input("How much is the cost for one year?")
    credits = input("How many credits are you enroled in?")
    while True:
        # Show your menu here.
        print("Welcome to the program! You are on the main menu")
        print("1 for Cost per Semester")
        print("2 for Cost per Month")
        print("3 for Cost per Day")
        print("4 for Cost per Credit")
        print("5 for Cost per Class")
        print("Q to Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            print("Exiting program now, goodbye!")
            break
        elif(choice == '1'):
            semester = cost_per_semester(annual_cost)
            print(f"One semester costs ${semester:,.2f}")
        elif(choice == '2'):
            month = cost_per_month(annual_cost)
            print(f"One month costs ${month:,.2f}")
        elif(choice == '3'):
            day = cost_per_day(annual_cost)
            print(f"One day costs ${day:,.2f}")
        elif(choice == '4'):
            credit = cost_per_credit(annual_cost, credits)
            print(f"Per credit hour costs ${credit:,.2f}")
        elif(choice == '5'):
            class_1 = cost_per_class(annual_cost, credits)
            print(f"One class of CS1430 costs ${class_1:,.2f}")
        


    

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
