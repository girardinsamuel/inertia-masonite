"""A InertiaProvider Service Provider."""
import os
from masonite.provider import ServiceProvider

from masonite.inertia.InertiaResponse import InertiaResponse
from masonite.inertia.commands.InstallCommand import InstallCommand


class InertiaProvider(ServiceProvider):
    """Masonite adapter for Inertia.js Service Provider."""

    wsgi = False

    def register(self):
        self.app.bind("Inertia", InertiaResponse(self.app))
        self.app.bind("InstallCommand", InstallCommand())

    def boot(self):
        app_path = os.path.join(os.path.dirname(__file__), "../snippets/static")

        self.publishes(
            {
                os.path.join(app_path, "mix-manifest.json"): "storage/static/js/mix-manifest.json",
                os.path.join(app_path, "app.js"): "storage/static/js/app.js",
                os.path.join(app_path, "pages/Index.vue"): "storage/static/js/pages/Index.vue"
                os.path.join(app_path, "pages/HelloWorld.vue"): "storage/static/js/pages/HelloWorld.vue"
            }, tag="app"
        )
