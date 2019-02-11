class Time:
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
def is_after(t1,t2):
    return(t1.hour,t1.minute,t1.second)>(t2.hour,t2.minute,t2.second)

time = Time()
time.hour = 9
time.minute = 50
time.second = 15

time1 = Time()
time1.hour = 10
time1.minute = 51
time1.second = 16

print(is_after(time1,time))




