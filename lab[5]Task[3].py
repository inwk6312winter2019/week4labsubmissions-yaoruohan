class Time:
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
def print_time(time):
    print("%.2d:%.2d:%.2d" %(time.hour,time.minute,time.second))

time = Time()
time.hour = 9
time.minute = 55
time.second = 10
print_time(time)


