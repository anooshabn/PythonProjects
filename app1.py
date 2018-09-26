__author__ = 'anushabn'

def ask_choice():
    choice = input("Do you want seconds (s) or years (y)?: ")
    return choice

def calculate_age():
    if ask_choice() == 's':
        age_in_years = input("Enter your age in years: ")
        age_sec = int(age_in_years) * 365 * 24 * 60 * 60
        return str(age_sec) + " seconds"
    else:
        age_in_seconds = input("Enter your age in seconds: ")
        age_yrs = int(age_in_seconds) / 60 / 60 / 24 / 365
        return str(age_yrs) + " years"

def user_age():
    print("Your age is {}".format(calculate_age()))

user_age()