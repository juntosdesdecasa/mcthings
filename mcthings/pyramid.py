# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi.block
from mcpi.vec3 import Vec3

from .thing import Thing


class Pyramid(Thing):
    height = 10

    def create(self):
        length = 2 * self.height - 1
        width = length

        for i in range(0, self.height):
            level = i
            p = self.position
            self.set_blocks(
                Vec3(p.x + level, p.y + level, p.z + level),
                Vec3(p.x + (length - 1) - level,
                     p.y + level,
                     p.z + (width - 1) - level),
                self.block)

        self._end_position = Vec3(p.x + (length - 1),
                                  p.y + self.height - 1,
                                  p.z + (width - 1)
                                  )


class PyramidHollow(Thing):
    height = 10
    thick = 2

    def create(self):
        outer = Pyramid(self.position, self._renderer, self)
        outer.height = self.height
        outer.block = self.block
        outer.create()
        self._end_position = outer.end_position
        inner_x = self.position.x + self.thick
        inner_y = self.position.y
        inner_z = self.position.z + self.thick
        inner = Pyramid(Vec3(inner_x, inner_y, inner_z), self._renderer, self)
        inner.block = mcpi.block.AIR
        inner.height = self.height - self.thick
        inner.create()
