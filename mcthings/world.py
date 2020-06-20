# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

# TODO: at some point this must be a real Singleton
import pickle


class World:
    """
    A world is a container for all the scenes built using McThings. Its mapping
    is direct to Minecraft world concept.

    Before adding Worlds to the World, it must be connected to a
    Minecraft server (fill the World.server attribute)
    """
    scenes = []

    @classmethod
    def connect(cls, server):
        # When the create->transform->render pipeline is complete remove next line
        World.server = server.mc
        World.drawing = server.drawing

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
        for thing in cls.things:
            thing.unbuild()

    @classmethod
    def load(cls, file_path):
        """ Load a scene from a file (but no build it yet) """
        World.scenes = pickle.load(open(file_path, "rb"))

    @classmethod
    def save(cls, file_path):
        """ Save a scene to a file """
        pickle.dump(World.scenes, open(file_path, "wb"))
