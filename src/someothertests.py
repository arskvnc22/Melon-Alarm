from datetime import datetime, timedelta

t= datetime.now()
print(t.strftime("%H:%M"))
print(t + timedelta(minutes=30))