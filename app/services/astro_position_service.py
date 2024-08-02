from libtad import AstronomyService
from libtad.datatypes.places import Coordinates, LocationId
from libtad.datatypes.time import TADDateTime
from libtad.datatypes.astro import AstronomyObjectType
from app.config import settings

class AstroPositionService:
    def __init__(self):
        self.service = AstronomyService("gTAaJ9UTA7", "04WxCo6NeWoJAA4dQiWy")

    def get_astro_position(self, object_type: AstronomyObjectType, coordinates: Coordinates, date: TADDateTime):
        place = LocationId("netherlands/amsterdam")
        
        return self.service.get_astronomical_info(AstronomyObjectType.Moon, place, date)
# todo
# .env
# correct params pass
# tests