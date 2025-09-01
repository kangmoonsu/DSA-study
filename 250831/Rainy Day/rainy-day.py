n = int(input())

class Info:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

weather_list = []

for _ in range(n):
    d, dy, w = input().split()
    i = Info(d, dy, w)
    weather_list.append(i)


sorted_weather = sorted(weather_list, key=lambda i: i.date)


for weather_info in sorted_weather:
    if weather_info.weather == "Rain":
        print(weather_info.date, weather_info.day, weather_info.weather)
        break
