# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

# TODO: at some point this must be a real Singleton
import pickle

from mcpi.vec3 import Vec3

from mcthings.blocks_memory import BlocksMemory
from mcthings.utils import build_schematic_nbt
from mcthings.world import World


class Scene:
    """
    A scene is a container for all the things built using McThings.
    A scene can be built, unbuilt and moved. There is only one scene
    in a program using McThings. Things built are added automatically to
    the Scene. A Scene can also be loaded from a file, and
    it can be saved to a file.

    Before adding Things to the Scene, it must be connected to a
    Minecraft server (fill the Scene.server attribute)
    """

    def __init__(self):
        self.things = []
        """ map with the things in the scene """
        self._decorators = []
        """ decorators for the scene """
        self._position = None
        """ position in the world of the scene """
        self._end_position = None
        """ end position in the world of the scene """

        World.add_scene(self)

    @property
    def end_position(self):
        """ end position of the thing """
        return self._end_position

    @property
    def position(self):
        """ initial position of the thing """
        return self._position

    def add(self, thing):
        """ Add a new thing to the scene """
        if not self.things:
            # The initial position of the scene is the position
            # of its first thing added
            self._position = thing.position
        self.things.append(thing)

    def add_decorator(self, decorator):
        """ Add a new decorator to the scene """
        self._decorators.append(decorator)

    def decorate(self):
        """
        Call all decorators for the current Scene

        :return:
        """

        for decorator in self._decorators:
            decorator(self).decorate()

    def build(self):
        """ Build all the things inside the Scene """
        for thing in self.things:
            thing.build()

        (min_pos, max_pos) = self.find_bounding_box()
        self._end_position = max_pos

    def unbuild(self):
        """ Unbuild all the things inside the Scene """
        for thing in self.things:
            thing.unbuild()

    def create(self):
        """ Create all the things inside the Scene """
        for thing in self.things:
            thing.create()

    def reposition(self, position):
        """
        Move all the things in the scene to a new relative position

        :param position: new position for the Scene
        :return:
        """

        # All the things inside the scene must be moved
        diff_x = position.x - self._position.x
        diff_y = position.y - self._position.y
        diff_z = position.z - self._position.z

        for thing in self.things:
            repos_x = thing.position.x + diff_x
            repos_y = thing.position.y + diff_y
            repos_z = thing.position.z + diff_z

            thing._position = (Vec3(repos_x, repos_y, repos_z))

    def move(self, position):
        """
        Move the scene to a new position

        :param position: new position
        :return:
        """

        self.unbuild()
        self.reposition(position)
        self.build()

    def load(self, file_path):
        """ Load a scene from a file (but no build it yet) """
        self.things = pickle.load(open(file_path, "rb"))
        if self.things:
            self._position = self.things[0].position

    def save(self, file_path):
        """ Save a scene to a file """

        def clean_memory(thing):
            for child in thing._children:
                clean_memory(child)
            thing._blocks_memory = BlocksMemory()

        # Clean the blocks_memory: it is not needed to recreate the scene
        for thing in self.things:
            clean_memory(thing)
        pickle.dump(self.things, open(file_path, "wb"))

        # Reload the memory
        self.create()

    def find_bounding_box(self):
        """ Compute the bounding box of the Scene """

        def update_box(box_pos_min, box_pos_max, pos):
            # Update box_pos_min and box_pos_max checking pos
            box_pos_min.x = pos.x if pos.x < box_pos_min.x else box_pos_min.x
            box_pos_min.y = pos.y if pos.y < box_pos_min.y else box_pos_min.y
            box_pos_min.z = pos.z if pos.z < box_pos_min.z else box_pos_min.z
            box_pos_max.x = pos.x if pos.x > box_pos_max.x else box_pos_max.x
            box_pos_max.y = pos.y if pos.y > box_pos_max.y else box_pos_max.y
            box_pos_max.z = pos.z if pos.z > box_pos_max.z else box_pos_max.z

            return box_pos_min, box_pos_max

        # Default init values
        min_pos = Vec3(self._position.x, self._position.y, self._position.z)
        max_pos = Vec3(self._position.x, self._position.y, self._position.z)

        # Find the bounding box for the scene
        for thing in self.things:
            min_pos, max_pos = update_box(min_pos, max_pos, thing.position)
            if thing.end_position:
                min_pos, max_pos = update_box(min_pos, max_pos, thing.end_position)

        return min_pos, max_pos

    def to_schematic(self, file_path, block_data=False):
        """
        Save the Scene into a Schematic file

        :param file_path: file in which to export the Scene in Schematic format
        :param block_data: extract blocks ids and data (much slower)
        :return: the Schematic object
        """

        (min_pos, max_pos) = self.find_bounding_box()

        build_schematic_nbt(min_pos, max_pos, block_data).write_file(file_path)
