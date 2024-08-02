from libtad import AstrodataService
from libtad.datatypes.places import Coordinates, LocationId
from libtad.datatypes.time import TADDateTime
from libtad.datatypes.astro import AstronomyObjectType

from app.config import settings

class AstroEventService:
    def __init__(self):
        self.service = AstrodataService(settings.ASTRO_API_ACCESS_KEY, settings.ASTRO_API_SECRET_KEY)

    def get_astro_event(self, object_type: AstronomyObjectType, coordinates: Coordinates, date: TADDateTime):
        place = LocationId(coordinates)
        
        return self.service.get_astrodata(object_type, place, date)
