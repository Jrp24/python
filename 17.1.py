from __future__ import print_function, division

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        total_seconds = hour * 3600 + minute * 60 + second
        self.seconds_since_midnight = total_seconds

    def __str__(self):
        hours, remainder = divmod(self.seconds_since_midnight, 3600)
        minutes, seconds = divmod(remainder, 60)
        return '%.2d:%.2d:%.2d' % (hours, minutes, seconds)

    def print_time(self):
        print(str(self))

    def time_to_int(self):
        return self.seconds_since_midnight

    def is_after(self, other):
        return self.seconds_since_midnight > other.seconds_since_midnight

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        total_seconds = self.seconds_since_midnight + other.seconds_since_midnight
        return int_to_time(total_seconds)

    def increment(self, seconds):
        total_seconds = self.seconds_since_midnight + seconds
        return int_to_time(total_seconds)

    def is_valid(self):
        if self.seconds_since_midnight < 0:
            return False
        return True

def int_to_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return Time(hours, minutes, seconds)

def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)

if __name__ == '__main__':
    main()

