from typing import Literal
from fastapi import APIRouter
from libtad.datatypes.places import Coordinates
from libtad.datatypes.time import TADDateTime
from libtad.datatypes.astro import AstronomyObjectType

from app.services.astro_position_service import AstroPositionService

object_type_map = {
    "Sun": AstronomyObjectType.Sun,
    "Moon": AstronomyObjectType.Moon,
    # Add other mappings as necessary
}

router = APIRouter()

@router.get("/astro_position")
def get_astro_position(
    object_type: Literal["Sun", "Moon"], 
    latitude: float,
    longitude: float,
    year: int,
    month: int,
    day: int
  ):
    coordinates = Coordinates(latitude, longitude)
    date = TADDateTime(year, month, day)

    service = AstroPositionService()

    result = service.get_astro_position(object_type, coordinates, date)

    return result
