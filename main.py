from apllication import salary
from apllication.db import people
from datetime import date
from freegames import pacman

if __name__ == "__main__":
    print(f"Сегодня: {date.today()}")
    people.get_employees()
    salary.calculate_salary(150, 30)
