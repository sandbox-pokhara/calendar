import questionary as q
from add import add_month, add_year, add_holiday

while (True):
    todo = q.select(
        "What do you want to do?",
        choices=[
            "Add a holiday",
            "Add a month",
            "Replace month",
            "Remove a holiday",
            "Nothing, just quit",
        ],
    ).ask()
    if (todo == "Add a holiday"):
        add_holiday()
    elif (todo == "Add a month"):
        add_month()
    elif (todo == "Add a year"):
        add_year()
    elif (todo == "Replace month"):
        print("Not implemented yet")
    elif (todo == "Remove a holiday"):
        print("Not implemented yet")
    elif (todo == "Nothing, just quit"):
        break
