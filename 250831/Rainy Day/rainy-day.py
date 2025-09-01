n = int(input())

class Info:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather

weather_list = []

for _ in range(n):
    d, dy, w = input().split()
    i = Info(d,dy,w)
    weather_list.append(i)

sorted_date = sorted(weather_list, key=lambda i: i.date)

for j in range(n):
    if weather_list[j].weather == "Rain":
        print(weather_list[j].date,weather_list[j].day,weather_list[j].weather)
        break


# Please write your code here.