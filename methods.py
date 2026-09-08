
"""Methods used in birthday_tracker.py which are not part of the methods used in main_menu()"""

import json
import calendar

path_json = 'data\\birthday.json'

buildStrDate = lambda year, month, day: f'{day} {calendar.month_name[month]} {year}'
createCode = lambda date: f'{str(date)[5:7]}{str(date)[8:10]}'


def load_data():
    """Load and return the data stored in json file"""
    with open(path_json, 'r') as file:
        return json.load(file)


def sort_two_lists(list_of_days, list_of_people, reverse=False):
    """Algorithm which uses a bubble sort to sort two same-length lists according to the value of the days / number"""

    """bubble sort technique in python by Dizzy Dotterel on Jan 17 2021"""
    n = len(list_of_days)

    # Traverse through all array elements
    for i in range(n - 1):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if not reverse:
                if list_of_days[j] > list_of_days[j + 1]:
                    list_of_days[j], list_of_days[j + 1] = list_of_days[j + 1], list_of_days[j]
                    list_of_people[j], list_of_people[j + 1] = list_of_people[j + 1], list_of_people[j]

            elif reverse:
                if list_of_days[j] < list_of_days[j + 1]:
                    list_of_days[j], list_of_days[j + 1] = list_of_days[j + 1], list_of_days[j]
                    list_of_people[j], list_of_people[j + 1] = list_of_people[j + 1], list_of_people[j]

    """end of borrowed code"""

    return list_of_days, list_of_people


def check_leap_year(year):
    """Check if the year is a leap year"""
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False