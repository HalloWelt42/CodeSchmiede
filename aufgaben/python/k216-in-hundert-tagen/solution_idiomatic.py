from datetime import datetime, timedelta

tag = datetime.strptime(input(), "%d.%m.%Y").date()
tage = int(input())
print((tag + timedelta(days=tage)).strftime("%d.%m.%Y"))
