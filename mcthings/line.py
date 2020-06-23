# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi.block
from mcpi.vec3 import Vec3

from .thing import Thing
from .world import World


class Line(Thing):

    width = 3
    length = 10

    def create(self):
        end_x = self.position.x + self.width - 1
        end_y = self.position.y - 1
        end_z = self.position.z + self.length - 1

        # Find the type of land block destroyed with the line
        self._block_empty = \
            mcpi.block.Block(World.renderer.get_block(Vec3(self.position.x, self.position.y-1, self.position.z)), 0)

        self.set_blocks(Vec3(self.position.x, self.position.y-1, self.position.z),
                        Vec3(end_x, end_y, end_z),
                        self.block.id)

        self._end_position = Vec3(end_x, end_y + 1, end_z)
