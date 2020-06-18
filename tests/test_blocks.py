#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3

from mcthings.blocks import Blocks
from tests.base import TestBaseThing


class Ve3(object):
    pass


class TestBlocks(TestBaseThing):
    """Test Blocks Thing"""

    def test_build(self):
        self.renderer.server._mc.postToChat("Building blocks")

        self.pos.z += 1
        blocks = Blocks(self.pos, self.renderer)
        blocks.width = 2
        blocks.height = 4
        blocks.length = 3
        blocks.build()
        assert blocks._chunks_memory[0].size == Vec3(2, 4, 3)
        assert len(blocks._chunks_memory[0].blocks_ids) == 2*3*4

        self.pos.z += 10
        blocks = Blocks(self.pos, self.renderer)
        blocks.build()

        blocks.move(Vec3(self.pos.x+5, self.pos.y, self.pos.z))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
