import trip, event, transportation
import datetime

def main():
    now = datetime.datetime.now()
    flight = transportation.Plane('DL188', 'DTW', 'LGA', '2:40', '4:40', 41, 'Confirmation', now)
    train = transportation.Train('Grand Central', 'Penn station', 'NJTransit', '2:40', '4:40', 41, 'Confirmation', now)
    ferry = transportation.Boat('Battery Park Dock 3', 'Jersey City Slip 7', 'Goldman Ferry', '2:40', '4:40', 41, 'Confirmation', now)
    uber = transportation.Boat('Columbia University', 'NYU', 'Uber', '2:40', '4:40', 41, 'Confirmation', now)
    print(flight)
    print(train)
    print(ferry)
    print(uber)

    NYC = trip.Trip()
    NYC.add_event(flight)
    NYC.add_event(train)
    out = NYC.get_all_events()
    print(out)

if __name__ == "__main__":
    main()