#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.block import Block
from mcpi.vec3 import Vec3

from mcthings.collage import Collage
from mcthings.world import World
from tests.base import TestBaseThing


class TestBlocks(TestBaseThing):
    """Test Collage Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building collage")

        self.pos.z += 1
        blocks = Collage(self.pos)
        blocks.build()
        assert len(blocks._blocks_memory.blocks) == 24
        assert blocks._blocks_memory.blocks[23].id == 42

        self.pos.z += 10
        blocks = Collage(self.pos)
        blocks.build()

        blocks.move(Vec3(self.pos.x+5, self.pos.y, self.pos.z))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
