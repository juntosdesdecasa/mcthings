#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi.block
from mcpi.vec3 import Vec3

from mcthings.block import Block
from mcthings.platform import Platform
from mcthings.world import World
from tests.base import TestBaseThing


class TestPlatform(TestBaseThing):
    """Test Platform Thing"""

    def test_build(self):
        self.renderer.server._mc.postToChat("Building a platform")

        self.pos.z += 1
        platform = Platform(self.pos, self.renderer)
        platform.top_size = 7
        platform.height = 20
        platform.build()

        block = Block(platform.end_position, self.renderer)
        block.block = mcpi.block.BEDROCK
        block.build()

        p = Vec3(platform.end_position.x, platform.end_position.y + 1, platform.end_position.z)
        World.server.entity.setTilePos(
            self.renderer.server._mc.getPlayerEntityId(self.BUILDER_NAME),
            p)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
