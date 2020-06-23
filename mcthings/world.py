# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

# TODO: at some point this must be a real Singleton


class World:
    """
    A world is a container for all the scenes built using McThings. Its mapping
    is direct to Minecraft world concept.

    Before adding Things to the World, it must have a renderer
    """
    scenes = []
    """ Scenes included in the world """
    renderer = None
    """ Render used to render the scenes """

    @classmethod
    def set_renderer(cls, renderer):
        cls.renderer = renderer

        # TODO: Hack for Minecraft renderer
        from mcthings.renderers.raspberry_pi import RaspberryPi
        if isinstance(renderer, RaspberryPi):
            World.server = renderer.mc
            World.drawing = renderer.drawing

    @classmethod
    def add_scene(cls, scene):
        """ Add a new scene to the world """
        cls.scenes.append(scene)

    @classmethod
    def first_scene(cls):
        """ Return the first scene used be default """
        return cls.scenes[0]

    @classmethod
    def build(cls):
        """ Build all the scenes inside the world """
        for scene in cls.scenes:
            scene.build()

    @classmethod
    def unbuild(cls):
        """ Unbuild all the scenes inside the world """
        for scene in cls.scene:
            scene.unbuild()
