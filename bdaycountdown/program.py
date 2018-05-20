import datetime


def get_birthday_from_user():
    print("when is your birthday")
    year = int(input("year [yyyy]: "))
    month = int(input("month [mm]: "))
    day = int(input("day [dd]: "))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print("your birthday was {} days ago, dummy.".format(-days))
    elif days > 0:
        print("your birthday isn\'t for {} more days, dummy.".format(days))
    else:
        print("guess you're one year closer to death.")


def main():
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)


main()
