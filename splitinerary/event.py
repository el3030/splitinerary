import datetime


class Event:
    """
    Event object. Sortable by datetime.

    Attributes:
        datetime: datetime.datetime object of when the user wants to arrive at the event, NOT NECESSARILY when the event starts 
            (e.g. user might arrive at the airport 2 hours before the flight departs)
    """

    def __init__(self, datetime):
        self.datetime = datetime

    def __lt__(self, other):
        return self.datetime < other.datetime

    def __eq__(self, other):
        return self.datetime == other.datetime

    def __str__(self) -> str:
        date = str(self.datetime.date())
        time = str(self.datetime.time())
        return f'date: {date}, time: {time}'
