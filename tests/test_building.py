#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi

from mcthings.building import Building
from mcthings.world import World
from tests.base import TestBaseThing


class TestBuilding(TestBaseThing):
    """Test Building Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building a building")

        pos = self.pos

        pos.x += 1

        building = Building(pos)
        building.block = mcpi.block.BEDROCK
        building.house_mirror = True
        building.build()

        Building(building.end_position).build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
