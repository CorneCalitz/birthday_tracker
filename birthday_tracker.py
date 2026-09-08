"""

This program is meant to track birthdays:

Ideas:
 - Save birthday and name of person in JSON/textfile
 - Check current day and date with birthday day and date
 - Notification should be sent to user, not the birthday person


    Goals:
    * Sorting the names and dates will also be nice
    * Allow for deletion of a person if needed
    * Create a tree as a learning exercise to allow for more optimal searches
    * Implement a search algorithm for the names
    TEST CHANGES
"""

import datetime

from methods import *


def main_menu():
    """Creates a menu and manages the navigation"""

    while True:
        check_current_date()

        print("\nBIRTHDAY TRACKER MENU")
        print("1. Input name and birthday")
        print("2. Upcoming birthdays")
        print("3. Search for person ")
        print("4. EXIT")

        response = input("->>>")

        if response == "1":
            print('Input name and birthday here')
            save_input()

        elif response == "2":
            print('Here is a list of upcoming names and birthdays:\n----------------------------')
            display_upcoming_bdates()

        elif response == '3':
            print("Search for person")
            search_person()

        elif response == "4":
            exit('Bye')

        else:
            print('No response listed above')


def save_input():
    """Saves the input to a json file"""

    person = dict()
    name = input("Input name: ").title()

    try:
        day = int(input("Input day of birth"))
        month = int(input('Input month of birth (number):'))
        year = int(input("Input year of birth:"))
        birth_date = datetime.date(year, month, day)
    except ValueError:
        print("Date is invalid!\nInput not saved")
        main_menu()
    else:

        person['name'] = name
        person['year'] = birth_date.year
        person['month'] = birth_date.month
        person['day'] = birth_date.day

        with open(path_json, 'r') as file:
            data = json.load(file)
            data.append(person)

        with open(path_json, 'w') as f:
            json.dump(data, f, indent=4)


def search_person():
    """Search for the person's name"""
    birthday_people = load_data()
    searched_name = input("Input the person's name: ").title()
    for person in birthday_people:
        if searched_name == person['name']:
            print(f'{person["name"]}\n{buildStrDate(person["year"], person["month"], person["day"])}\n')
            break


def check_current_date():
    """Will check if any date (day, month) in dictionary corresponds with today's date. Runs on launch."""

    birthday_people = load_data()
    # Creates a code used to compare month and day of birthday date and current date
    current_date = datetime.date.today()
    current_date_code = createCode(current_date)

    message = False

    for person in birthday_people:
        dob = datetime.date(person['year'], person['month'], person['day'])
        birthday_date_code = createCode(dob)
        if birthday_date_code == current_date_code:
            message = True
            age = current_date.year - dob.year
            print(
                f"It is {person['name']}'s birthday today\n{buildStrDate(person['year'], person['month'], person['day'])}"
                f"\n{age} years old\n")

    if not message:
        print("There are no birthdays today")


def display_upcoming_bdates():
    """Sort the dates according to upcoming birthdays"""
    birthday_people = load_data()

    days_until = []
    people_until = []

    current_date = datetime.date.today()
    for person in birthday_people:
        # We set the dob year the same as the current year since we only want to figure out the exact days within one
        # year
        dob = datetime.date(current_date.year, person['month'], person['day'])

        delta = dob - current_date
        days = delta.days
        if days < 0:
            if check_leap_year(current_date.year):
                days_until.append(days + 366)
                people_until.append(person)
            else:
                days_until.append(days + 365)
                people_until.append(person)
        else:
            days_until.append(days)
            people_until.append(person)

    days_until, people_until = sort_two_lists(days_until, people_until)
    people_until.reverse()
    days_until.reverse()
    
    for i in range(len(days_until)):

        output = f'{people_until[i]["name"]}' \
                 f'\n{buildStrDate(people_until[i]["year"], people_until[i]["month"], people_until[i]["day"])} '

        if days_until[i] == 0:
            print(output)
            print(f'Happy birthday {people_until[i]["name"]}\n')

        else:
            print(output)
            print(days_until[i], 'day(s) remain\n')
    print('----------------------------')


if __name__ == '__main__':
    main_menu()
