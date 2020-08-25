""" Web Routes """
from masonite.routes import Get, Post

from app.http.controllers.InertiaController import InertiaController
from app.http.controllers.TestController import TestController


ROUTES = [
    Get("/test", TestController.show),
    Get("/", "InertiaController@inertia"),
]
