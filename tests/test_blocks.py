#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import sys
import unittest

import mcpi.block
from mcpi.vec3 import Vec3

from mcthings.block import Block
from mcthings.blocks import Blocks
from tests.base import TestBaseThing


class Ve3(object):
    pass


class TestBlocks(TestBaseThing):
    """Test Blocks Thing"""

    def test_build(self):
        self.renderer.server._mc.postToChat("Building blocks")

        self.pos.x += 1
        blocks = Blocks(self.pos, self.renderer)
        blocks.width = 2
        blocks.height = 4
        blocks.length = 3
        blocks.build()
        assert len(blocks._blocks_memory.blocks  ) == 2*3*4

        # check the first and last block
        init_block = Block(blocks.position, self.renderer)
        init_block.block = mcpi.block.GOLD_BLOCK
        init_block.build()
        end_block = Block(blocks.end_position, self.renderer)
        end_block.block = mcpi.block.GOLD_BLOCK
        end_block.build()

        self.pos.z += 10
        blocks = Blocks(self.pos, self.renderer)
        blocks.build()

        blocks.move(Vec3(self.pos.x+5, self.pos.y, self.pos.z))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
