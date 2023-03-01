import event


class Transportation(event.Event):
    def __init__(self, departure_time, arrival_time, cost=0, confirmation_code=None, *args, **kw):
        self.cost = cost
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.confirmation_code = confirmation_code
        super().__init__(*args, **kw)

    def __str__(self) -> str:
        return super().__str__() + f', departure time: {self.departure_time}, arrival time: {self.arrival_time}'


class Plane(Transportation):
    def __init__(self, flight_number, departure_terminal=None, arrival_terminal=None, *args, **kw):
        self.flight_number = flight_number
        self.departure_terminal = departure_terminal
        self.arrival_terminal = arrival_terminal
        super().__init__(*args, **kw)

    def __str__(self) -> str:
        return super().__str__() + f', FLIGHT, flight_number: {self.flight_number}'


class Train(Transportation):
    def __init__(self, departure_station, arrival_station, train_line=None, *args, **kw):
        self.train_line = train_line
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        super().__init__(*args, **kw)

    def __str__(self) -> str:
        return super().__str__() + f', TRAIN, departure_station: {self.departure_station}, arrival_station: {self.arrival_station}'


class Boat(Transportation):
    def __init__(self, departure_terminal, arrival_terminal, route=None,  *args, **kw):
        self.route = route
        self.departure_terminal = departure_terminal
        self.arrival_terminal = arrival_terminal
        super().__init__(*args, **kw)

    def __str__(self) -> str:
        return super().__str__() + f', BOAT, departure_terminal: {self.departure_terminal}, arrival_terminal: {self.arrival_terminal}'


class Car(Transportation):
    def __init__(self, departure_location, arrival_location, company=None, *args, **kw):
        self.departure_location = departure_location
        self.arrival_location = arrival_location
        self.company = company
        super().__init__(*args, **kw)

    def __str__(self) -> str:
        return super().__str__() + f', BOAT, departure_location: {self.departure_location}, arrival_location: {self.arrival_location}'
