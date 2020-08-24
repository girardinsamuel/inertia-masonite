"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get("/", "WelcomeController@inertia").name("welcome"),
    Get("/helloworld", "WelcomeController@helloworld"),
]
