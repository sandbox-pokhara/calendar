from file import create_month, create_red_day
import questionary as q
from template import normal_day, red_day, blank_day

MONTH_CHOICES = [
    "1 January",
    "2 February",
    "3 March",
    "4 April",
    "5 May",
    "6 June",
    "7 July",
    "8 August",
    "9 September",
    "10 October",
    "11 November",
    "12 December",
]

WEEKDAY_CHOICES = [
    "1 Sunday",
    "2 Monday",
    "3 Tuesday",
    "4 Wednesday",
    "5 Thursday",
    "6 Friday",
    "7 Saturday",
]


def ask_month_info():
    start_weekday = q.select(
        "What day does the month start?",
        choices=WEEKDAY_CHOICES,
    ).ask()
    start_weekday = int(start_weekday.split(" ")[0])
    end_day = q.select(
        "What is the end day of the month?",
        choices=[
            "28",
            "29",
            "30",
            "31",
            "32",
        ],
    ).ask()
    end_day = int(end_day)
    return start_weekday, end_day


def get_month_info_lib(year, month):
    import calendar
    start_weekday = calendar.weekday(year, month, 1)
    # Mon is 0, Sun is 6
    # make Sun 1, Sat 7
    start_weekday = (start_weekday + 1) % 7 + 1
    end_day = calendar.monthrange(year, month)[1]
    return start_weekday, end_day


def add_month() -> bool:
    year = q.text("What year?").ask()
    year = int(year)
    month_str = q.select(
        "What month?",
        choices=MONTH_CHOICES,
    ).ask()
    month = int(month_str.split(" ")[0])
    monthName = month_str.split(" ")[1]
    use_library = q.select(
        "Provide month details.",
        choices=[
            "Manual entry.",
            "Use library.",
        ],
    ).ask()
    use_library = use_library == "Use library."
    if not use_library:
        start_weekday, end_day = ask_month_info()
    else:
        start_weekday, end_day = get_month_info_lib(year, month)

    days = [blank_day] * 36  # days[0] not used
    days_int = [i for i in range(-36, 0)]
    current_day = 1
    current_idx = start_weekday
    while current_day <= end_day and current_idx <= 35:
        if current_idx % 7 == 0:
            days[current_idx] = red_day.format(day=current_day)
            days_int[current_idx] = current_day
        else:
            days[current_idx] = normal_day.format(day=current_day)
            days_int[current_idx] = current_day
        current_day += 1
        current_idx += 1
    current_idx = 1
    while current_day <= end_day and current_idx <= 4:
        days[current_idx] = normal_day.format(day=current_day)
        days_int[current_idx] = current_day
        current_day += 1
        current_idx += 1

    create_month(year, month, monthName, start_weekday,
                 end_day, days, days_int)
    return True


def add_year() -> bool:
    year = q.text("What year?").ask()
    year = int(year)
    print("Not implemented yet")
    return True


def add_holiday() -> bool:
    year = q.text("What year?").ask()
    year = int(year)
    month_str = q.select(
        "What month?",
        choices=MONTH_CHOICES,
    ).ask()
    month = int(month_str.split(" ")[0])
    day = q.text("What day?").ask()
    day = int(day)
    reason = q.text("Why?").ask()
    create_red_day(year, month, day, reason)
    return True
