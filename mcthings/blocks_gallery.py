# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi

from mcpi.vec3 import Vec3

from .thing import Thing


class BlocksGallery(Thing):
    # https://www.minecraftinfo.com/idlist.htm
    MAX_BLOCK_NUMBER = 247

    def create(self):
        """
        Show all possible block types in a line
        :return:
        """

        for i in range(1, self.MAX_BLOCK_NUMBER):
            p = self.position
            self.set_block(Vec3(p.x + i, p.y, p.z), i)

        self._end_position = Vec3(p.x + self.MAX_BLOCK_NUMBER - 1, p.y, p.z)
