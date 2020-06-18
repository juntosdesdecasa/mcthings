# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author/s (©): Alvaro del Castillo
import math

import mcpi
import mcpi.block
from nbt import nbt

from mcpi.vec3 import Vec3

from mcthings.memory_chunk import MemoryChunk
from mcthings.thing import Thing
from mcthings.world import World


class Schematic(Thing):
    _blocks_field = 'Blocks'
    _data_field = 'Data'
    file_path = None
    """ file path for the schematic file """
    rotate_degrees = 0
    """ rotate the schematic """
    change_blocks = {mcpi.block.AIR.id: mcpi.block.AIR.id}
    """ Change a block with other """

    def find_bounding_box(self):
        """ In a Schematic the bounding box is inside the file data """

        schematic = nbt.NBTFile(self.file_path, 'rb')

        size_x = schematic["Width"].value
        size_y = schematic["Height"].value
        size_z = schematic["Length"].value

        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        self._end_position = Vec3(init_x + size_x,
                                  init_y + size_y,
                                  init_z + size_z)

        return self.position, self.end_position

    def create(self):
        if not self.file_path:
            RuntimeError("Missing file_path param")

        schematic = nbt.NBTFile(self.file_path, 'rb')
        size_x = schematic["Width"].value
        size_y = schematic["Height"].value
        size_z = schematic["Length"].value

        chunk = MemoryChunk(Vec3(size_x, size_y, size_z), schematic[self._data_field], schematic[self._blocks_field])
        self.chunks_memory.append(chunk)

    def rotate(self, degrees):
        """
        Rotate the thing in the x,z space. Blocks data is not preserved.

        In a Schematic, we load the data in memory, rotate it and build it

        :param degrees: degrees to rotate (90, 180, 270)
        :return:
        """

        valid_degrees = [90, 180, 270]

        if degrees not in [90, 180, 270]:
            raise RuntimeError("Invalid degrees: %s (valid: %s) " % (degrees, valid_degrees))

        self.rotate_degrees = degrees

        self.build()
