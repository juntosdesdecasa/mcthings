# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import math

from mcpi.vec3 import Vec3

from .thing import Thing


class Platform(Thing):
    top_size = 3  # square platform at the top
    height = 10  # tower height

    def create(self):
        p = self.position

        # base of the tower
        base_x = p.x + math.floor(self.top_size/2)
        base_z = p.z + math.floor(self.top_size/2)
        self.set_blocks(Vec3(base_x, p.y, base_z),
                        Vec3(base_x, p.y + self.height - 1, base_z),
                        self.block.id)

        # Top
        self.set_blocks(Vec3(p.x, p.y + self.height, p.z),
                        Vec3(p.x + self.top_size - 1, p.y + self.height, p.z + self.top_size - 1),
                        self.block.id)

        self._end_position = Vec3(p.x + self.top_size - 1,
                                  p.y + self.height,
                                  p.z + self.top_size - 1)
