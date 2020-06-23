# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo
from mcpi.vec3 import Vec3

from .thing import Thing


class Wall(Thing):
    height = 5
    length = 10
    width = 2

    def create(self):
        self.set_blocks(
            Vec3(self.position.x, self.position.y, self.position.z),
            Vec3(self.position.x + self.length - 1,
                 self.position.y + self.height - 1,
                 self.position.z + self.width - 1),
            self.block.id)
