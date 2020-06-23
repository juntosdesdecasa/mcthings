# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

from mcpi.vec3 import Vec3

from .thing import Thing


class Blocks(Thing):
    width = 3  # x
    height = 2  # y
    length = 4  # z

    def create(self):
        p = self.position
        self._end_position = Vec3(p.x + self.width - 1, p.y + self.height - 1, p.z + self.length - 1)
        # self.set_blocks(Vec3(p.x, p.y, p.z), self._end_position, self.block.id)
        self.set_blocks(self._end_position, Vec3(p.x, p.y, p.z), self.block.id)
