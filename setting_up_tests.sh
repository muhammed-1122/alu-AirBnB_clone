#!/bin/bash

# Ensure we are in the models directory
mkdir -p models

# Create State
echo '#!/usr/bin/python3
"""Module for State class."""
from models.base_model import BaseModel

class State(BaseModel):
    """Represent a state."""
    name = ""' > models/state.py

# Create City
echo '#!/usr/bin/python3
"""Module for City class."""
from models.base_model import BaseModel

class City(BaseModel):
    """Represent a city."""
    state_id = ""
    name = ""' > models/city.py

# Create Amenity
echo '#!/usr/bin/python3
"""Module for Amenity class."""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represent an amenity."""
    name = ""' > models/amenity.py

# Create Review
echo '#!/usr/bin/python3
"""Module for Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represent a review."""
    place_id = ""
    user_id = ""
    text = ""' > models/review.py

# Create Place
echo '#!/usr/bin/python3
"""Module for Place class."""
from models.base_model import BaseModel

class Place(BaseModel):
    """Represent a place."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []' > models/place.py

# Set executable permissions
chmod +x models/state.py models/city.py models/amenity.py models/review.py models/place.py
