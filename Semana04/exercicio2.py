from datetime import datetime, timedelta

data = datetime.today()
data = data + timedelta(days=3, weeks=2)

print(data)