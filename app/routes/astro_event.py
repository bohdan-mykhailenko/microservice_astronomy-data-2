from fastapi import APIRouter
from libtad.datatypes.places import Coordinates
from libtad.datatypes.time import TADDateTime
from libtad.datatypes.astro import AstronomyObjectType

from app.services.astro_event_service import AstroEventService

router = APIRouter()

@router.get("/astro_event")
def get_astro_event(object_type: AstronomyObjectType, latitude: float, longitude: float, year: int, month: int, day: int):
    coordinates = Coordinates(latitude, longitude)
    date = TADDateTime(year, month, day)

    service = AstroEventService()
    
    result = service.get_astro_event(object_type, coordinates, date)

    return result
