#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi

from mcthings.block import Block
from mcthings.world import World
from tests.base import TestBaseThing


class TestLines(TestBaseThing):
    """Test Lines Thing"""

    def test_build(self):
        self.renderer.server._mc.postToChat("Building lines of blocks")

        pos = self.pos
        blocks_number = 5

        # Line in incresing x
        block_pos = mcpi.vec3.Vec3(pos.x+1, pos.y, pos.z)
        for x in range(0, blocks_number):
            block_pos.x += 1
            Block(block_pos, self.renderer).build()

        # Line in decresing x
        block_pos = mcpi.vec3.Vec3(pos.x+1, pos.y, pos.z)
        for x in range(1, blocks_number):
            block_pos.x -= 1
            Block(block_pos, self.renderer).build()

        # Line in incresing y
        block_pos = mcpi.vec3.Vec3(pos.x+1, pos.y, pos.z)
        for y in range(1, blocks_number):
            block_pos.y += 1
            Block(block_pos, self.renderer).build()

        # Line in decresing y
        block_pos = mcpi.vec3.Vec3(pos.x+1, pos.y, pos.z)
        for y in range(1, blocks_number):
            block_pos.y -= 1
            Block(block_pos, self.renderer).build()

        # Line in incresing z
        block_pos = mcpi.vec3.Vec3(pos.x+1, pos.y, pos.z)
        for z in range(1, blocks_number):
            block_pos.z += 1
            Block(block_pos, self.renderer).build()

        # Line in decresing z
        block_pos = mcpi.vec3.Vec3(pos.x+1, pos.y, pos.z)
        for z in range(1, blocks_number):
            block_pos.z -= 1
            Block(block_pos, self.renderer).build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
