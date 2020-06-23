#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3

from mcthings.block import Block
from mcthings.world import World
from tests.base import TestBaseThing


class TestBlock(TestBaseThing):
    """Test Block Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building two blocks")

        pos = self.pos

        pos.x += 1
        block = Block(pos)
        block.build()

        assert len(block._blocks_memory.blocks) == 1

        pos.x += 3
        block = Block(pos)
        block.build()
        block.unbuild()

        block.move(Vec3(pos.x+5, pos.y, pos.z))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
