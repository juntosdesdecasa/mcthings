#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi
from mcpi.vec3 import Vec3
from mcthings.decorators.light_decorator import LightDecorator

from mcthings.town import Town
from mcthings.world import World
from tests.base import TestBaseThing


class TestTown(TestBaseThing):
    """Test Town Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building a town")

        pos = self.pos

        pos.x += 1

        town = Town(pos)
        town.block = mcpi.block.BEDROCK
        town.build()

        town = Town(Vec3(pos.x-5, pos.y, pos.z))
        town.block = mcpi.block.BEDROCK
        town.house_mirror = True
        town.build()

        town.add_decorator(LightDecorator)
        town.decorate()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
