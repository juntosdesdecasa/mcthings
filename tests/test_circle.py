#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi

from mcthings.circle import Circle
from mcthings.world import World
from tests.base import TestBaseThing


class TestCircle(TestBaseThing):
    """Test Circle Thing"""

    def test_build(self):
        self.renderer.server._mc.postToChat("Building a circle")

        pos = self.pos

        radius = 10
        pos.z += 20

        circle = Circle(pos, self.renderer)
        circle.radius = radius
        circle.block = mcpi.block.BEDROCK
        circle.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
