class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.month:02d}/{self.day:02d}/{self.year:04d}"

    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"

    def is_leap_year(self):
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def is_valid(self):
        if self.year == 0:
            return False

        if self.month < 1 or self.month > 12:
            return False

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.is_leap_year():
            days_in_month[1] = 29

        max_day = days_in_month[self.month - 1]
        if self.day < 1 or self.day > max_day:
            return False

        return True

    def tomorrow(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.is_leap_year():
            days_in_month[1] = 29

        max_day = days_in_month[self.month - 1]

        self.day += 1

        if self.day > max_day:
            self.day = 1
            self.month += 1

            
            if self.month > 12:
                self.month = 1
                self.year += 1
