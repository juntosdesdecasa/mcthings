# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

from mcpi.vec3 import Vec3

from .thing import Thing


class Block(Thing):

    def create(self):
        self.set_block(Vec3(self.position.x, self.position.y, self.position.z), self.block.id)
        self._end_position = self.position
