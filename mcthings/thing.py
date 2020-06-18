# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo
import logging
import math

import mcpi.block
import mcpi.vec3

from ._version import __version__

from .memory_chunk import MemoryChunk
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

        self._chunks_memory = []  # List of MemoryChunks
        self._chunks_positions = []  # List of positions of the chunks
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
                Scene()  # Scene add itself to the World

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
        self._chunks_memory.append(MemoryChunk(size_region(pos, pos), [block], [data]))
        self._chunks_positions.append(pos)

    def set_blocks(self, init_pos, end_pos, block, data=None):

        def blocks_in_cuboid(min_pos, max_pos):
            size = 0
            size_x = max_pos.x - min_pos.x + 1
            size_y = max_pos.y - min_pos.y + 1
            size_z = max_pos.z - min_pos.z + 1
            for y in range(0, size_y):
                for z in range(0, size_z):
                    for x in range(0, size_x):
                        size += 1
            return size

        blocks = [block for i in range(0, blocks_in_cuboid(init_pos, end_pos))]
        data = [data for i in range(0, blocks_in_cuboid(init_pos, end_pos))]

        self._chunks_memory.append(MemoryChunk(size_region(init_pos, end_pos), blocks, data))
        self._chunks_positions.append(init_pos)

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

        for i in range(0, len(self._chunks_memory)):
            self._renderer.render(self._chunks_memory[i], self._chunks_positions[i])

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
        Rotate the thing in the x,z space using the memory chunks.

        :param degrees: degrees to rotate (90, 180, 270)
        :return:
        """

        valid_degrees = [90, 180, 270]

        if degrees not in [90, 180, 270]:
            raise RuntimeError("Invalid degrees: %s (valid: %s) " % (degrees, valid_degrees))

        cos_degrees = math.cos(math.radians(degrees))
        sin_degrees = math.sin(math.radians(degrees))

        def rotate_x(pos_x, pos_z):
            return pos_x * cos_degrees - pos_z * sin_degrees

        def rotate_z(pos_x, pos_z):
            return pos_z * cos_degrees + pos_x * sin_degrees

        if self.end_position is None:
            raise RuntimeError("Can rotate a thing %s without the end_position" % self)

        for i in range(0, len(self._chunks_memory)):
            chunk = self._chunks_memory[i]
            chunk_pos = self._chunks_positions[i]

            # Add the rotated blocks
            for y in range(0, chunk.size.y):
                for z in range(0, chunk.size.z):
                    for x in range(0, chunk.size.x):
                        i = x + chunk.size.x * z + (chunk.size.x * chunk.size.z) * y
                        b = chunk.blocks_ids[i]
                        d = chunk.blocks_data[i]
                        rotated_x = chunk_pos.x + rotate_x(x, z)
                        rotated_z = chunk_pos.z + rotate_z(x, z)
                        # TODO: remove the not rotated block
                        # The final order of the blocks must follow the
                        # rotated_y -> rotated_z -> rotated_x
                        # We can save all block position and store them ordered later
                        # But it is needed only in set_blocks cases
                        self.set_block(mcpi.Vec3(rotated_x, chunk_pos.y + y, rotated_z), b, d)
                        self._end_position = mcpi.vec3.Vec3(rotated_x, chunk_pos.y + y, rotated_z)

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
            decorator.decorate(self)
            for child in self._children:
                decorator.decorate(child)

    def find_bounding_box(self):
        """ Compute the bounding box of the Thing """

        return self.position, self.end_position
