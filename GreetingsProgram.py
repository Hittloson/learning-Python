import datetime

currentTime = datetime.datetime.now()
year = datetime.datetime.now().year

if currentTime.hour < 12:
    print("Good Morning")

elif 12 <= currentTime.hour < 16:
    print("Good Afternoon")

else:
    print("Good Evening")
