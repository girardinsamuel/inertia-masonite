""" Web Routes """
from masonite.routes import Get, Post

from app.http.controllers.InertiaController import InertiaController


ROUTES = [
    Get("/", "InertiaController@show"),
]
