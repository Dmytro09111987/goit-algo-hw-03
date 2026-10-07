from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        entry_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.now().date()
        delta = today - entry_date
        return delta.days

    except ValueError:
        print("Error: Date mast be in YYYY-MM-DD format")
        return None
result = get_days_from_today("2021-10-09")
print(result)