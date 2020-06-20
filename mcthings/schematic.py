# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author/s (©): Alvaro del Castillo

import mcpi.block
from nbt import nbt

from mcpi.vec3 import Vec3

from mcthings.thing import Thing


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

        init_pos = self.position

        for y in range(0, size_y):
            for z in range(0, size_z):
                for x in range(0, size_x):
                    i = x + size_x * z + (size_x * size_z) * y
                    block_id = schematic[self._blocks_field][i]
                    block_data = schematic[self._data_field][i] & 0b00001111  # lower 4 bits
                    block_pos = Vec3(init_pos.x + x, init_pos.y + y, init_pos.z + z)
                    if block_id in self.change_blocks:
                        block_id = self.change_blocks[block_id]
                    self.set_block(block_pos, block_id, block_data)
