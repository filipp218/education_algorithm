from datetime import datetime

class Trip:

    def __init__(self, start, end, lenght):
        start = datetime.strptime(start ,"%H:%M")
        end = datetime.strptime(end ,"%H:%M")
        diff = end - start
        self.time_continue = diff.total_seconds()/3600
        self.lenght = round(float(lenght))

    def speed(self):
        speed = self.lenght / float(self.time_continue)
        return round(speed)


class Driver:

    def __init__(self, name):
        self.name = name
        self.mile = 0
        self.all_time = 0

    def add_trip(self, way):
        if 5<way.speed()<100:
            self.mile += way.lenght
            self.all_time += way.time_continue

    def __repr__(self):
        return str(self.name)

    def status(self):
        if self.mile > 0 and self.all_time>0:
            return (self.mile, round(self.mile/self.all_time), self.name)
        return (self.mile, 0, self.name)


all_driver = {}
with open("text.txt", "r") as text:
    for line in text.readlines():
        a = [i for i in line.split(' ')]
        if a[0] == 'Driver':
            b = a[1][0:-1] # это нужно чтобы отрезать хвостик "/n", он прилипает к имени. типа "Dan/n"
            all_driver[b] = Driver(b)
        elif a[0] == 'Trip':
            way = Trip(a[2], a[3], a[4])
            all_driver[a[1]].add_trip(way)

result = []
for i in all_driver:
    result.append(all_driver[i].status())

result = sorted(result,reverse=True)
with open("result.txt", "w") as text:
    for mile, speed, name in result:
        if speed > 0:
            words = f'{name} : {mile} miles @ {speed} mph\n'
        else:
            words = f'{name} : {mile} miles\n'
        text.write(words)
