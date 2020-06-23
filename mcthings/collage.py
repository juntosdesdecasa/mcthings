# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

from mcpi.vec3 import Vec3
import mcpi.block

from .thing import Thing


class Collage(Thing):
    width = 3  # x
    height = 2  # y
    length = 4  # z
    change_blocks = [mcpi.block.BEDROCK, mcpi.block.SAND, mcpi.block.GOLD_BLOCK, mcpi.block.IRON_BLOCK]

    def create(self):
        p = self.position
        count = 0
        for y in range(0, self.height):
            for z in range(0, self.length):
                for x in range(0, self.width):
                    block = self.block
                    if self.block != self._block_empty:
                        block = self.change_blocks[count % len(self.change_blocks)]
                    self.set_block(Vec3(p.x + x, p.y + y, p.z + z), block.id)
                    count += 1

        self._end_position = Vec3(p.x + self.width - 1, p.y + self.height - 1, p.z + self.length - 1)
