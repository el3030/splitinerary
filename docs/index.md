# Welcome to Splitinerary's documentation!

## Installation

Shell command to install the library from PyPI:
```
pip install splitinerary
```

## Usage

After installing the library, import the splitinerary module:
```
import splitinerary
```
Or import specific objects to use:
```
from splitinerary import Trip, Plane
```

Example program for a simple trip:
```
from splitinerary import Trip, Plane
import datetime

now = datetime.datetime.now()
date = now.date()
trip = Trip()
event = Event(now)

trip.add_event(event)

events = trip.get_all_events()
```

For a full list of objects and functions, please see documentation.

```eval_rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
```
## Indices and tables
```eval_rst
* :ref:`genindex`
* :ref:`modindex`
```