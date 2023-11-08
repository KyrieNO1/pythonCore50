import time
from datetime import datetime
class Clock:
    """digital clock"""

    def __init__(self, hour = 0, minute = 0, second = 0):
        """initialing"""
        self.sec = second
        self.min = minute
        self.hour = hour

    def run(self):
        """running"""
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.sec += 1
            if self.min == 60:
                self.min = 0
                self.min += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        """show time"""
        return f'{self.hour:2d}:{self.min:2d}:{self.sec:2d}'

# 获取当前时间
current_time = datetime.now()

# 提取时、分和秒
current_hour = current_time.hour
current_minute = current_time.minute
current_second = current_time.second

print(f"The current time is: {current_hour}:{current_minute}:{current_second}")


clock = Clock(current_hour, current_minute, current_second)

while True:
    print(clock.show())
    time.sleep(1)
    clock.run()