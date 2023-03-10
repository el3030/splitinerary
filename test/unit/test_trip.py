from splitinerary import Event, Trip

import unittest
import datetime


class TestAddEvent(unittest.TestCase):
    def test_add_event_success(self):
        # arrange
        now = datetime.datetime.now()
        date = now.date()
        trip = Trip()
        event = Event(now)

        expected_dates_list = [date]
        expected_dates_dict = {date: [event]}

        # act
        trip.add_event(event)

        # assert
        self.assertListEqual(trip.dates_list, expected_dates_list)
        self.assertDictEqual(trip.dates_dict, expected_dates_dict)


class TestGetEventsOnDate(unittest.TestCase):
    def test_get_events_on_eventful_date_success(self):
        # arrange
        now = datetime.datetime.now()
        date = now.date()
        trip = Trip()
        event = Event(now)
        trip.add_event(event)
        expected_events_list = [event]

        # act
        events = trip.get_events_on_date(date)

        # assert
        self.assertListEqual(events, expected_events_list)

    def test_get_events_on_uneventful_date_success(self):
        # arrange
        now = datetime.datetime.now()
        date = now.date()
        trip = Trip()

        # act
        events = trip.get_events_on_date(date)

        # assert
        self.assertIsNone(events)


class TestGetEventfulDates(unittest.TestCase):
    def test_get_eventful_dates_success(self):
        # arrange
        now = datetime.datetime.now()
        date = now.date()
        trip = Trip()
        event = Event(now)
        trip.add_event(event)
        expected_dates_list = [date]

        # act
        dates = trip.get_eventful_dates()

        # assert
        self.assertListEqual(dates, expected_dates_list)

    def test_get_no_eventful_dates_success(self):
        # arrange
        trip = Trip()

        # act
        dates = trip.get_eventful_dates()

        # assert
        self.assertIsNone(dates)


class TestGetAllEvents(unittest.TestCase):
    def test_get_all_events_success(self):
        # arrange
        now = datetime.datetime.now()
        trip = Trip()
        event = Event(now)
        trip.add_event(event)
        expected_events_list = [event]

        # act
        events = trip.get_all_events()

        # assert
        self.assertListEqual(events, expected_events_list)

    def test_get_no_events_success(self):
        # arrange
        trip = Trip()

        # act
        events = trip.get_all_events()

        # assert
        self.assertIsNone(events)


class TestGetNextEvent(unittest.TestCase):
    def test_get_next_event_success(self):
        # arrange
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)
        yesterday = now - datetime.timedelta(days=1)
        trip = Trip()
        yesterdayss_event = Event(yesterday)
        tomorrows_event = Event(tomorrow)
        trip.add_event(yesterdayss_event)
        trip.add_event(tomorrows_event)

        # act
        next_event = trip.get_next_event()

        # assert
        self.assertEqual(next_event, tomorrows_event)

    def test_get_next_event_after_lastsuccess(self):
        # arrange
        now = datetime.datetime.now()
        yesterday = now - datetime.timedelta(days=1)
        trip = Trip()
        yesterdayss_event = Event(yesterday)
        trip.add_event(yesterdayss_event)

        # act
        next_event = trip.get_next_event()

        # assert
        self.assertIsNone(next_event)
