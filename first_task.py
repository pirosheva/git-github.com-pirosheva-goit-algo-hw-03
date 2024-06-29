from datetime import datetime

def get_days_from_today(date: str):
        try:
            return datetime.now().date() - datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            print("Not valid date format")
    
date = input("Enter a date in format(year-month-day): ")
print(get_days_from_today(date))