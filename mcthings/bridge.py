# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

from math import floor

from mcpi.vec3 import Vec3

from .thing import Thing


class Bridge(Thing):
    large = 5
    height = None
    width = 1

    def create(self):
        for z in range(0, self.width):
            self.build_row(z)

        self._end_position = Vec3(self.position.x + self.large - 1,
                                  self.position.y + self.height,
                                  self.position.z + self.width - 1
                                  )

    def build_row(self, z):
        # large = 2 * height - 1
        max_height = floor((self.large + 1) / 2)
        if self.height is None:
            self.height = max_height

        for x in range(0, self.large):
            if x < max_height:
                y = x
            elif x == max_height and self.large % 2 == 0:
                y = max_height - 1
            else:
                y = y - 1

            final_y = y

            if self.height and y >= self.height - 1:
                final_y = self.height - 1

            self.set_block(
                Vec3(self.position.x + x, self.position.y + final_y, self.position.z + z),
                self.block.id)
