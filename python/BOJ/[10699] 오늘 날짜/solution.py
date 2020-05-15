import datetime
KST = datetime.timezone(datetime.timedelta(hours=9))
now = datetime.datetime.now(tz=KST)
print(now.strftime('%Y-%m-%d'))