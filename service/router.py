from fastapi import APIRouter

from service.api.image import image
from service.api.random import random_beer
from service.api.beer import beer
from service.api.beers import beers

api_router = APIRouter()

api_router.get("/images/{filename:path}")(image)
api_router.get("/beers/random")(random_beer)
api_router.get("/beers/{beer_id}")(beer)
api_router.get("/beers")(beers)
