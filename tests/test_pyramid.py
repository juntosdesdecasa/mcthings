#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi
from mcpi.vec3 import Vec3

from mcthings.pyramid import Pyramid, PyramidHollow
from mcthings.world import World
from tests.base import TestBaseThing

FLAT_WORLD_GROUND_HEIGHT = 4


class TestPyramid(TestBaseThing):
    """Test Pyramid Thing"""

    def test_build(self):
        self.renderer.server._mc.postToChat("Building a pyramid")

        pos = self.pos

        pyramid = Pyramid(pos, self.renderer)
        pyramid.height = 5
        pyramid.block = mcpi.block.SAND
        pyramid.build()

        pyramid = Pyramid(pyramid.end_position, self.renderer)
        pyramid.block = mcpi.block.BEDROCK
        pyramid.height = 3
        pyramid.build()
        # Let's move the last pyramid to the ground
        pyramid.move(Vec3(pyramid.position.x, FLAT_WORLD_GROUND_HEIGHT,
                          pyramid.position.z))

        pyramid = PyramidHollow(Vec3(pos.x + 20, pos.y, pos.z), self.renderer)
        pyramid.block = mcpi.block.WOOD
        pyramid.build()

        pyramid.to_schematic("schematics/pyramid_hollow.schematic")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
