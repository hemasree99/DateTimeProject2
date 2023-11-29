import datetime

class CustomDateTime:
    def __init__(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        if year is None:
            current_datetime = datetime.datetime.utcnow()
            self._datetime = current_datetime.replace(hour=hour, minute=minute, second=second)
        else:
            self._datetime = datetime.datetime(year, month, day, hour, minute, second)

    @classmethod
    def from_iso_format(cls, iso_string):
        try:
            dt = datetime.datetime.fromisoformat(iso_string)
            return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        except ValueError as e:
            raise ValueError(f"Invalid ISO-format: {iso_string}") from e

    def to_iso_format(self):
        return self._datetime.isoformat()

    def to_human_readable_format(self):
        return self._datetime.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def validate_date(year, month, day):
        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False

    @classmethod
    def date_difference(cls, date1, date2, unit='days'):
        if not isinstance(date1, cls) or not isinstance(date2, cls):
            raise ValueError("Both the dates must be instances of CustomDateTime")
        
        delta = date1._datetime - date2._datetime

        if unit == 'days':
            return delta.days
        elif unit == 'weeks':
            return delta.days // 7
        elif unit == 'months':
            return (date1.year - date2.year) * 12 + date1.month - date2.month
        else:
            raise ValueError("Entered wrong unit. Use 'days', 'weeks', or 'months'.")

    @staticmethod
    def date_from_string(date_string):
        try:
            dt = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
            return CustomDateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        except ValueError as e:
            raise ValueError(f"Entered Invalid date string format: {date_string}") from e

    # Properties to access individual parts of the datetime object
    @property
    def year(self):
        return self._datetime.year

    @property
    def month(self):
        return self._datetime.month

    @property
    def day(self):
        return self._datetime.day

    @property
    def hour(self):
        return self._datetime.hour

    @property
    def minute(self):
        return self._datetime.minute

    @property
    def second(self):
        return self._datetime.second
    
# Example usage:
# Creating instances using different methods
dt1 = CustomDateTime(1999, 7, 14, 12, 30, 45)
dt2 = CustomDateTime.from_iso_format("1999-07-14T12:30:45")

# Printing in different formats
print("ISO-Format:", dt1.to_iso_format())
print("Human Readable Format:", dt1.to_human_readable_format())

# Accessing individual parts of the datetime object
print("Year:", dt1.year)
print("Month:", dt1.month)
print("Day:", dt1.day)
print("Hour:", dt1.hour)
print("Minute:", dt1.minute)
print("Second:", dt1.second)

# Validating a date
print("Is 1999-07-14 a valid date?", CustomDateTime.validate_date(1999, 7, 14))
print("Is 2022-04-12 a valid date?", CustomDateTime.validate_date(2022, 4, 12))

# Date difference
dt3 = CustomDateTime(2000, 4, 12)
print("Number of days between dt1 and dt3:", CustomDateTime.date_difference(dt1, dt3, unit='days'))
print("Nuumber of weeks between dt1 and dt3:", CustomDateTime.date_difference(dt1, dt3, unit='weeks'))
print("Number of months between dt1 and dt3:", CustomDateTime.date_difference(dt1, dt3, unit='months'))

# Creating a date from a string
dt4 = CustomDateTime.date_from_string("2002-08-1 08:45:30")
print("Date created from string:", dt4.to_human_readable_format())