#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi

from mcthings.sphere import Sphere
from mcthings.sphere import SphereHollow
from mcthings.world import World
from tests.base import TestBaseThing


class TestSphere(TestBaseThing):
    """Test Sphere Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building a sphere")

        pos = self.pos

        radius = 10
        pos.z += 20

        sphere = Sphere(pos)
        sphere.radius = radius
        sphere.block = mcpi.block.IRON_BLOCK
        sphere.build()

        World.renderer.post_to_chat("Building a hollow sphere")
        pos.x += 20
        sphere = SphereHollow(pos)
        sphere.radius = radius
        sphere.block = mcpi.block.WOOD
        sphere.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
