"""A InertiaProvider Service Provider."""
import os
from masonite.provider import ServiceProvider

from masonite.inertia.InertiaResponse import InertiaResponse
from masonite.inertia.commands.InstallCommand import InstallCommand
from masonite.inertia.commands.DemoCommand import DemoCommand


class InertiaProvider(ServiceProvider):
    """Masonite adapter for Inertia.js Service Provider."""

    wsgi = False

    def register(self):
        self.app.bind("Inertia", InertiaResponse(self.app))
        self.app.bind("InstallCommand", InstallCommand())
        self.app.bind("DemoCommand", DemoCommand())

    def boot(self):
        snippets_path = os.path.join(os.path.dirname(__file__), "../snippets")
        app_path = os.path.join(snippets_path, "static")

        self.publishes(
            {
                os.path.join(
                    app_path, "mix-manifest.json"
                ): "storage/static/js/mix-manifest.json",
                os.path.join(app_path, "app.js"): "storage/static/js/app.js",
                os.path.join(
                    app_path, "pages/Index.vue"
                ): "storage/static/js/pages/Index.vue",
                os.path.join(
                    app_path, "pages/HelloWorld.vue"
                ): "storage/static/js/pages/HelloWorld.vue",
            },
            tag="app",
        )

        self.publishes(
            {
                os.path.join(
                    snippets_path, "controllers/InertiaController.py"
                ): "app/controllers/InertiaController.py",
            },
            tag="demo",
        )

        # TODO append two routes
