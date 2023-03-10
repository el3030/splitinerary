import datetime


class Trip:
    """
    Trip object.

    Attributes:
        dates_list (list): list (that can be sorted) of datetime.date, used to
            keep track of which dates have events on them.
        dates_dict (dict): {key, value}={datetime.date : event.Event}
            keys can be used to see if date exists in trip, values are lists
            (that can be sorted) of each day's events.
    """

    def __init__(self):
        self.dates_list = []
        self.dates_dict = {}

    def add_event(self, event):
        """
        Add an (already made) event to the Trip.
        This involves adding the date of the event to self.dates_list and
            adding the event to self.dates_dict[date].

        Parameters:
            event (event.Event):  The event to be added to the Trip.
        Returns:
            None
        """
        date = event.datetime.date()
        if date not in self.dates_dict:
            self.dates_list.append(date)
            self.dates_dict[date] = []
        self.dates_dict[date].append(event)

    def get_events_on_date(self, date):
        """
        Returns of the events on a certain day in order of start time.

        Parameters:
            date (datetime.date):  the date whose events are to be returned.
        Returns:
            times_list (List[(datetime.time, events.Event)]): sorted list of
            events on the input date if it exists, else None.
        """
        if date not in self.dates_dict:
            return None
        else:
            self.dates_dict[date].sort()
            return self.dates_dict[date]

    def get_eventful_dates(self):
        """
        Print all of the dates that have an event on them in order of start
            time.

        Parameters:
            None
        Returns:
            dates_list (List[datetime.date]): sorted list of dates that have
            events on them if it exists, else None.

        """
        if not self.dates_list:
            return None
        self.dates_list.sort()
        return self.dates_list

    def get_all_events(self):
        """
        Returns all events in the trip in order of start time.

        Parameters:
            None
        Returns:
            all_events (List[event.Event]): sorted list of all events in the
            trip.
        """
        if not self.dates_dict:
            return None
        all_events = []
        for events in self.dates_dict.values():
            all_events.extend(events)
        all_events.sort()
        return all_events

    def get_next_event(self):
        """
        Returns the next event that will take place for any user.

        Parameters:
            None
        Returns:
            event (event.Event): the next event that will take place for any
            user if it exists, else None.
        """
        now = datetime.datetime.now()
        all_events = self.get_all_events()
        for event in all_events:
            if event.datetime < now:
                continue
            return event
        return None
