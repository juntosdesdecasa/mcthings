# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi.block
from mcpi.vec3 import Vec3

from ._version import __version__

from .blocks_memory import BlocksMemory, BlockMemory
from .scene import Scene
from .utils import build_schematic_nbt, extract_region, size_region
from .world import World


class Thing:
    """ base class for all objects in mcthings library """

    block = mcpi.block.BRICK_BLOCK
    """ block type used by the thing. Default to BRICK_BLOCK """
    _block_empty = mcpi.block.AIR
    """ block type used to remove blocks in this Thing """

    def __init__(self, position, renderer, parent=None, scene=None):
        """
        Create a thing
        :param position: build position
        :param parent: parent Thing in which this one is included
        :param renderer: renderer to use to render the Thing
        :param scene: scene in which this Thing is included
        """

        self._blocks_memory = BlocksMemory()
        self._children = []
        self._decorators = []
        self._end_position = None
        self._parent = parent
        self._position = None
        self._scene = scene
        self._renderer = renderer

        if position:
            self._position = mcpi.vec3.Vec3(position.x, position.y, position.z)

        if scene is None:
            # If no Scenes exists yet, create a new one
            if not World.scenes:
                Scene(self._renderer)  # Scene add itself to the World

            """ Use the default  Scene """
            self._scene = World.first_scene()

        # Add then thing built to the scene
        if parent is None:
            self._scene.add(self)

        # McThing version which created this Thing
        self._version = __version__

    @property
    def end_position(self):
        """ end position of the thing """
        return self._end_position

    @property
    def position(self):
        """ initial position of the thing """
        return self._position

    @property
    def parent(self):
        """ parent Thing in which this one is included """
        return self._position

    @property
    def scene(self):
        """ scene which this thing is included """
        return self._scene

    def add_child(self, child):
        """ Add a children to this Thing  """
        self._children.append(child)

    def set_block(self, pos, block, data=None):
        self._blocks_memory.set_block(pos, block, data)

    def set_blocks(self, init_pos, end_pos, block):
        """ Add a cuboid with the same block for all blocks and without specific data"""
        self._blocks_memory.set_blocks(init_pos, end_pos, block)

    def create(self):
        """
        Create the Thing in memory (BlocksMemory)
        :return:
        """

    def render(self):
        """
        Render the Thing from memory (BlocksMemory) to show it

        :param renderer: renderer to use to show the Thing
        :return:
        """

        self._renderer.render(self._blocks_memory)
        for child in self._children:
            child.render()

    def build(self):
        """
        Build the thing and show it using the renderer at position coordinates

        :return:
        """

        self.create()
        self.render()

    def unbuild(self):
        """
        Unbuild the thing in Minecraft

        :return:
        """

        block = self.block
        self.block = self._block_empty
        self._blocks_memory.blocks = []
        self.build()
        self.block = block

    def move(self, position):
        """
        Move the thing to a new position

        :param position: new position
        :return:
        """

        self.unbuild()
        self._position = position
        self.build()

    def rotate(self, degrees):
        """
        Rotate the thing in the x,z space using the blocks memory.

        :param degrees: degrees to rotate (90, 180, 270)
        :return:
        """

        self._blocks_memory.rotate(degrees, self.position)

        # Update the position and end_position after the rotation
        init_pos, end_pos = self._blocks_memory.find_init_end_pos()
        self._position = init_pos
        self._end_position = end_pos

    def to_schematic(self, file_path, blocks_data=False):
        """
        Convert the Thing to a Schematic Object

        :file_path: file in which to export the Thing in Schematic format
        :blocks_data: include blocks data (much slower)
        :return: the Schematic object
        """

        build_schematic_nbt(self.position, self.end_position, blocks_data).write_file(file_path)

    def add_decorator(self, decorator):
        """
        Add a new Decorator to be called once the Thing is decorated

        :param decorator: a Decorator to be called
        :return:
        """
        self._decorators.append(decorator)

    def decorate(self):
        """
        Call all decorators for the current Thing

        :return:
        """
        for decorator in self._decorators:
            decorator(self).decorate()
            for child in self._children:
                decorator.decorate(child)

    def find_bounding_box(self):
        """ Compute the bounding box of the Thing """

        return self.position, self.end_position
