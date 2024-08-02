from libtad import AstrodataService
from libtad.datatypes.places import Coordinates, LocationId
from libtad.datatypes.time import TADDateTime
from libtad.datatypes.astro import AstronomyObjectType
    
coordinates = Coordinates(59.743, 10.204)
place = LocationId(coordinates)
date = TADDateTime(2020, 11, 26)
service = AstrodataService("gTAaJ9UTA7", "04WxCo6NeWoJAA4dQiWy")

result = service.get_astrodata(AstronomyObjectType.Sun, place, date)

service2 = AstronomyService("accessKey", "secretKey")

result2 = service.get_astronomical_info(AstronomyObjectType.Moon, place, date)
