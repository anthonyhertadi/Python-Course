import time
import datetime

print("Hello!!!")
while True:
    print("ENTER YOUR BIRTHDATE!!! (use numbers only!)")
    year = int(input("YEAR : "))
    month = int(input("MONTH : "))
    date1 = int(input("DATE : "))
    x = datetime.datetime(year, month, date1)
    print(x)
    time.sleep(1)
    print("Today is...")
    today = datetime.date.today()
    print(today)
    print("Your Age is")