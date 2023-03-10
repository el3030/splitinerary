# splitinerary 📝🛫

Splitinerary is a collaborative itinerary library in Python.

[![](https://img.shields.io/github/license/el3030/splitinerary)](https://opensource.org/license/mit/)
[![](https://img.shields.io/github/issues/el3030/splitinerary)](https://github.com/el3030/splitinerary/issues)


## Overview

Coordinating a group to go on a trip together is difficult because some people may fly to the same destination from different origins, some people may split off mid-trip to go somewhere else and rejoin, and some people might be staying in different places (with relatives, for example). This python program will be the core functionality for an app that allows users to work together to create a collaborative itinerary.

- Trips are objects that have one or more users associated with it.
- Each trip will have events inside of it like flights, hotels, trains, AirBnBs, concerts, etc. that each user can associate him or herself with.
- Each even has more granular information like flight number for flights, address for hotels and airbnbs, station for trains, etc.  
- Each event can also have a dollar amount so costs are kept track of.

The end result is a comprehensive itinerary where every person in the trip can see who is doing what at any given point in time.

## Details

It uses a Makefile as a command registry, with the following commands:

- `make`: list available commands
- `make develop`: install and build this library and its dependencies using `pip`
- `make build`: build the library using `setuptools`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make format`: autoformat this library using `black`
- `make test`: run automated tests with `unittest`
- `make coverage`: run automated tests with `unittest` and collect coverage information
